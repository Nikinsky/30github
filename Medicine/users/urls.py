from django.urls import path, include
from .views import *

urlpatterns = [

    path('patient_mainpage/', PatientMainPageView.as_view(), name='patient_mp'),
    path('doctor_mainpage/', DoctorMainPageView.as_view(), name='doctor_mp'),

    path('doctor_profile/', DoctorUserProfileListView.as_view(), name='doctor_profile'),
    path('doctor_profile_update/<int:pk>/', DoctorProfileUpdateListView.as_view(), name='doctor_profile-update'),
    path('doctor_list/', DoctorListView.as_view(), name='doctor-list'),
    path('doctor_detail/<int:pk>/', DoctorDetailListView.as_view(), name='doctor-detail'),

    #    path('generate-slots/', GenerateSlotsView.as_view(), name='generate-slots'),

    path('slots/', ConsultationSlotListView.as_view(), name='all-slots'),
    path('slots/available/', AvailableConsultationSlotListView.as_view(), name='available-slots'),
    path('bookings/', BookingListView.as_view(), name='all-bookings'),
    path('bookings/create/', BookingCreateView.as_view(), name='create-booking'),

    path('register_patient/', RegisterView.as_view(), name='register-patient'),
    path('register_doctor/', RegisterDoctorView.as_view(), name='register-doctor'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('feedback_create', FeedbackCreateViewAPI.as_view(), name='feedback_create'),
    path('feedback_list', FeedbackListViewAPI.as_view(), name='feedback_create'),

]


