from rest_framework import generics, viewsets
from .serializers import *
from rest_framework.response import Response
from .models import ConsultationSlot, Booking


class MainPageListView(generics.ListAPIView):
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer


#
# # Список всех слотов (свободных и занятых)
# class ConsultationSlotListView(generics.ListAPIView):
#     queryset = ConsultationSlot.objects.all()
#     serializer_class = ConsultationSlotSerializer
#
# # Список только доступных слотов для конкретного врача
# class AvailableConsultationSlotListView(generics.ListAPIView):
#     serializer_class = ConsultationSlotSerializer
#
#     def get_queryset(self):
#         doctor_id = self.request.query_params.get('doctor')
#         if doctor_id:
#             return ConsultationSlot.objects.filter(doctor_id=doctor_id, is_booked=False)
#         return ConsultationSlot.objects.filter(is_booked=False)
#
# # Создание нового бронирования
# class BookingCreateView(generics.CreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
#
# # Список всех бронирований
# class BookingListView(generics.ListAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer