from django.urls import path
from . import views

urlpatterns = [
    # 의사 목록을 보여주는 URL 패턴
    path('doctor_list/', views.doctor_list, name='doctor_list'),
    # 각 의사의 상세 정보를 보여주는 URL 패턴
    path('doctor/search/', views.doctor_search, name='doctor_search'),
    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('appointment_request/', views.appointment_request, name='appointment_request'),
    path('appointment_list/', views.appointment_list, name='appointment_list'),
    path('accept_appointment/<int:appointment_id>/', views.accept_appointment, name='accept_appointment'),
    # path('doctor_detail/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
]
