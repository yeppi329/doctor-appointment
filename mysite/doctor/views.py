from datetime import datetime, timedelta
from django.shortcuts import render,HttpResponseRedirect,get_object_or_404, reverse
from django.db.models import Q
from django.http import HttpResponse
from .models import AppointmentRequest, Doctor, Patient

def search_doctor_by_datetime(datetime_input):
    target_time = datetime.strptime(datetime_input, '%Y-%m-%dT%H:%M')
    weekday = target_time.weekday()

    if weekday == 0:  # 월요일
        doctors = Doctor.objects.filter(
            monday_start__lte=target_time.time(),
            monday_end__gte=target_time.time()
        )
    elif weekday == 1:  # 화요일
        doctors = Doctor.objects.filter(
            tuesday_start__lte=target_time.time(),
            tuesday_end__gte=target_time.time()
        )
    elif weekday == 2:  # 수요일
        doctors = Doctor.objects.filter(
            wednesday_start__lte=target_time.time(),
            wednesday_end__gte=target_time.time()
        )
    elif weekday == 3:  # 목요일
        doctors = Doctor.objects.filter(
            thursday_start__lte=target_time.time(),
            thursday_end__gte=target_time.time()
        )
    elif weekday == 4:  # 금요일
        doctors = Doctor.objects.filter(
            friday_start__lte=target_time.time(),
            friday_end__gte=target_time.time()
        )
    elif weekday == 5:  # 토요일
        doctors = Doctor.objects.filter(
            saturday_start__lte=target_time.time(),
            saturday_end__gte=target_time.time()
        )
    elif weekday == 6:  # 일요일
        doctors = Doctor.objects.filter(
            sunday_start__lte=target_time.time(),
            sunday_end__gte=target_time.time()
        )
    else:
        doctors = Doctor.objects.none()  # 아무 결과도 없음
        
    print("doctors:",doctors)
    return doctors

def search_doctor(query, datetime_input):
    doctors = Doctor.objects.all()

    if query:
        query_parts = query.split()
        query_condition = Q()

        for part in query_parts:
            query_condition &= (
                Q(name__icontains=part) | 
                Q(hospital_name__icontains=part) |
                Q(departments__name__icontains=part)|
                Q(non_insurance_services__name__icontains=part)
            )
        doctors = doctors.filter(query_condition)

    if datetime_input:
        doctors = search_doctor_by_datetime(datetime_input).filter(pk__in=doctors)

    return doctors

def doctor_list(request):
    doctor_list = Doctor.objects.all()
    context = {'doctor_list': doctor_list}
    return render(request, 'doctor/doctor_list.html', context)

def doctor_search(request):
    query = request.GET.get('query')
    datetime_input = request.GET.get('datetime_input')
    doctors = search_doctor(query, datetime_input)
    doctors = doctors.distinct()

    context = {
        'query': query,
        'datetime_input': datetime_input,
        'doctors': doctors,
    }
    print("context:",context)
    return render(request, 'doctor/doctor_search.html', context)

def doctor_detail(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    context = {
        'doctor': doctor,
    }
    return render(request, 'doctor/doctor_detail.html', context)

def appointment_request(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        doctor_name = request.POST.get('doctor_name')
        requested_time_str = request.POST.get('requested_time')
        
        # 문자열을 datetime 객체로 변환
        requested_time = datetime.strptime(requested_time_str, '%Y-%m-%dT%H:%M')

        try:
            patient = Patient.objects.get(name=patient_name)
        except Patient.DoesNotExist:
            return HttpResponse("Patient not found.")

        try:
            doctor = Doctor.objects.get(name=doctor_name)
        except Doctor.DoesNotExist:
            return HttpResponse("Doctor not found.")

        # Create an appointment request
        appointment_request = AppointmentRequest(
            patient=patient,
            doctor=doctor,
            request_datetime=requested_time
        )
        expiration_time = appointment_request.calculate_expiration_time()
        appointment_request.save()

        if expiration_time:
            return HttpResponse(
                f"Appointment request created successfully!<br>"
                f"Appointment Request ID: {appointment_request.id}<br>"
                f"Patient Name: {patient.name}<br>"
                f"Doctor Name: {doctor.name}<br>"
                f"Requested Time: {requested_time}<br>"
                f"Expiration Time: {expiration_time}"
            )
        else:
            return HttpResponse("Doctor is not available during the requested time.")
    
    return render(request, 'doctor/appointment_request.html')

def search_appointments_by_doctor(doctor_name):
    try:
        doctor = Doctor.objects.get(name=doctor_name)
        appointments = AppointmentRequest.objects.filter(doctor=doctor)
        return appointments
    except Doctor.DoesNotExist:
        return None

def accept_appointment(request, appointment_id):
    try:
        appointment = AppointmentRequest.objects.get(pk=appointment_id)
        appointment.accepted = True
        appointment.save()
    except AppointmentRequest.DoesNotExist:
        pass

    return HttpResponseRedirect(reverse('appointment_list'))
   
# def appointment_list(request):
#     appointments = AppointmentRequest.objects.all()
#     context = {'appointments': appointments}
#     print("context:",context)
#     return render(request, 'doctor/appointment_list.html', context)
def appointment_list(request):
    doctor_name = request.GET.get('doctor_name')

    if doctor_name:
        if request.method == 'POST' and 'accept_request' in request.POST:
            # 수락된 요청의 ID를 받아와서 해당 예약 요청의 accepted 값을 True로 변경
            request_id = request.POST.get('request_id')
            appointment_request = AppointmentRequest.objects.get(pk=request_id)
            appointment_request.accepted = True
            appointment_request.save()

        appointments = search_appointments_by_doctor(doctor_name)

        # 수락되지 않은 예약만 필터링하여 표시
        appointments = appointments.filter(accepted=False)

        if appointments is None:
            return HttpResponse("의사를 찾을 수 없습니다.")
    else:
        appointments = AppointmentRequest.objects.all()

    context = {
        'appointments': appointments,
        'doctor_name': doctor_name,
    }
    return render(request, 'doctor/appointment_list.html', context)

