from django.urls import path, include
from .views import *

urlpatterns = [
    path('main_page', MainPageListView.as_view(), name='main_page-list'),

    path('slots/', ConsultationSlotListView.as_view(), name='all-slots'),
    path('slots/available/', AvailableConsultationSlotListView.as_view(), name='available-slots'),
    path('bookings/', BookingListView.as_view(), name='all-bookings'),
    path('bookings/create/', BookingCreateView.as_view(), name='create-booking'),
]