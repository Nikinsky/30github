from django.urls import path, include
from .views import *


urlpatterns = [
    path('doctor_profile/', DoctorUserProfileListView.as_view(), name='doctor_profile'),
    path('doctor_list/', DoctorListView.as_view(), name='doctor-list'),
    path('doctor_detail/<int:pk>/', DoctorDetailListView.as_view(), name='doctor-detail'),

]