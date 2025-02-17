from django.urls import path, include
from .views import *


urlpatterns = [
    path('doctor_profile/', DoctorUserProfileListView.as_view(), name='doctor_profile'),
    path('doctor_list/', DoctorListView.as_view(), name='doctor-list'),
    path('doctor_detail/<int:pk>/', DoctorDetailListView.as_view(), name='doctor-detail'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('feedback_create', FeedbackCreateViewAPI.as_view(), name='feedback_create'),
    path('feedback_list', FeedbackListViewAPI.as_view(), name='feedback_create'),

]