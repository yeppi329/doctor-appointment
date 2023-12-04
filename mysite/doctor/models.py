from django.db import models
from datetime import datetime, timedelta


class Patient(models.Model):
    name = models.CharField(max_length=100)

class Department(models.Model):
    name = models.CharField(max_length=100)
    

class NonInsuranceService(models.Model):
    name = models.CharField(max_length=100)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)

    monday_start = models.TimeField(blank=True, null=True)
    tuesday_start = models.TimeField(blank=True, null=True)
    wednesday_start = models.TimeField(blank=True, null=True)
    thursday_start = models.TimeField(blank=True, null=True)
    friday_start = models.TimeField(blank=True, null=True)
    saturday_start = models.TimeField( blank=True, null=True)
    sunday_start = models.TimeField(blank=True, null=True)
    
    monday_end = models.TimeField(blank=True, null=True)
    tuesday_end = models.TimeField(blank=True, null=True)
    wednesday_end = models.TimeField(blank=True, null=True)
    thursday_end = models.TimeField(blank=True, null=True)
    friday_end = models.TimeField(blank=True, null=True)
    saturday_end = models.TimeField( blank=True, null=True)
    sunday_end = models.TimeField(blank=True, null=True)
    
    lunch_start = models.TimeField(blank=True, null=True)
    lunch_end = models.TimeField(blank=True, null=True)
    
    departments = models.ManyToManyField(Department, related_name='doctors', blank=True)
    non_insurance_services = models.ManyToManyField(NonInsuranceService, related_name='doctors', blank=True, null=True)

class AppointmentRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    request_datetime = models.DateTimeField()
    expiration_datetime = models.DateTimeField()
    accepted = models.BooleanField(default=False)  # 수락 여부를 저장하는 필드
    
    def calculate_expiration_time(self):
        # 의사의 영업 시간을 기준으로 진료 요청의 만료 시간을 계산합니다.
        
        # 예약 요청된 날짜의 요일을 가져옵니다.
        weekday = self.request_datetime.weekday()
        doctor = self.doctor

        # 각 요일에 대한 의사의 영업 시간을 가져옵니다.
        doctor_working_hours = {
            0: {'start': doctor.monday_start, 'end': doctor.monday_end},  # 월요일
            1: {'start': doctor.tuesday_start, 'end': doctor.tuesday_end},  # 화요일
            2: {'start': doctor.wednesday_start, 'end': doctor.wednesday_end},  # 수요일
            3: {'start': doctor.thursday_start, 'end': doctor.thursday_end},  # 목요일
            4: {'start': doctor.friday_start, 'end': doctor.friday_end},  # 금요일
            5: {'start': doctor.saturday_start, 'end': doctor.saturday_end},  # 토요일
            6: {'start': doctor.sunday_start, 'end': doctor.sunday_end},  # 일요일
        }

        start_time = doctor_working_hours[weekday]['start']
        end_time = doctor_working_hours[weekday]['end']
        
        if start_time <= self.request_datetime.time() <= end_time:
            # 예약 요청 시간이 의사의 영업 시간 내에 있다면, 만료 시간을 20분 후로 설정합니다.
            self.expiration_datetime = self.request_datetime + timedelta(minutes=20)
            
            lunch_start = doctor.lunch_start
            lunch_end = doctor.lunch_end
            
            if lunch_start is not None and lunch_end is not None:
                if lunch_start <= self.request_datetime.time() <= lunch_end:
                    # 요청 시간이 점심시간 안에 있다면, 만료 시간을 점심시간 종료 후 15분으로 설정합니다.
                    self.expiration_datetime = self.request_datetime.replace(
                        hour=lunch_end.hour,
                        minute=lunch_end.minute
                    ) + timedelta(minutes=15)
        else:
            # 영업 시간 이후에 예약한 경우 -> 영업시간 이후라는 것이 구분이 필요함 => 영업 종료 ~ 밤12시 ~ 영업 시작
            next_day_weekday = (weekday + 1) % 7
            next_day_working_hours = doctor_working_hours[next_day_weekday]
            next_day_start_time = next_day_working_hours['start']

            if next_day_start_time < start_time:
                # 1. 영업종료 후 ~ 밤 12시 사이에 예약한 경우 (+15분)
                self.expiration_datetime = self.request_datetime.replace(
                    hour=next_day_start_time.hour,
                    minute=next_day_start_time.minute,
                ) + timedelta(minutes=15)
            else:
                # 2. 밤 12시 ~ 영업종료 후 사이에 예약한 경우 (+15분)
                self.expiration_datetime = self.request_datetime.replace(
                    hour=next_day_start_time.hour,
                    minute=next_day_start_time.minute,
                ) + timedelta(minutes=15)
                self.expiration_datetime += timedelta(days=1)
        
        return self.expiration_datetime