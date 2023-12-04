# Mysite

Mysite는 Django 및 SQLite를 사용하여 진료 예약 관리 시스템을 구축하는 프로젝트입니다.
- Django,SQLite를 사용한 프로젝트 입니다.

## 설치 및 설정

### 환경 설정

- Python을 설치합니다.
- 가상 환경을 생성하고 활성화합니다:

    ```    
    C:\projects>C:\venvs\mysite\Scripts\activate
    (mysite) C:\projects>cd mysite
    ```

### 프로젝트 설치
- 제공드린 압축파일을 원하는 폴더에 풀어주세요.

### 프로젝트 실행
- Djnago 프로젝트 디렉토리로 이동하여 종속성 셋팅을 합니다.

    ```
    pip install -r requirements/requirements.txt
    ```

- 데이터베이스 마이그레이션을 진행합니다..

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

- 서버를 실행합니다.

    ```
    python manage.py runserver
    ```

- 브라우저를 통해 'http://127.0.0.1:8000/' 에 접속하여 확인합니다.

## 모델 설명

- Patient: 환자 정보
- Department: 의사의 진료과목
- NonInsuranceService: 의사의 비급여진료과목 
- Doctor: 의사 정보와 영업 시간
- AppointmentRequest: 예약 관련 정보

## URL
- Doctor List: /api/doctor_list/에서 의사 목록 확인 가능
- Doctor Search: /api/doctor/search/에서 의사 검색 및 정보 확인 가능
- Appointment Request: /api/appointment_request/에서 예약을 요청 진행
- Appointment List: /api/appointment_list/에서 예약 목록 확인 및 수락 진행 여부 확인 가능