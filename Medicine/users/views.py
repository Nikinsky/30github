from rest_framework import generics, viewsets, status, permissions
from .serializers import *
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth.models import update_last_login
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import *
from rest_framework.response import Response
#from .services import generate_consultation_slots
#from .serializers import GenerateSlotsSerializer



class RegisterView(generics.GenericAPIView):
    """Регистрация нового пользователя с выдачей токенов"""
    serializer_class = RegisterPatientSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Генерация токенов
        refresh = RefreshToken.for_user(user)
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response(
            {
                "message": "User registered successfully.",
                "tokens": tokens,
            },
            status=status.HTTP_201_CREATED,
        )

class RegisterDoctorView(generics.GenericAPIView):
    """Регистрация нового пользователя с выдачей токенов"""
    serializer_class = RegisterDoctorSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Генерация токенов
        refresh = RefreshToken.for_user(user)
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response(
            {
                "message": "User registered successfully.",
                "tokens": tokens,
            },
            status=status.HTTP_201_CREATED,
        )

class LoginView(generics.GenericAPIView):
    """Авторизация пользователя по email с выдачей токенов"""
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {"error": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = UserProfile.objects.get(email=email)
        except UserProfile.DoesNotExist:
            return Response(
                {"error": "Invalid email or password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        user = authenticate(username=user.username, password=password)
        if user is None:
            return Response(
                {"error": "Invalid email or password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh = RefreshToken.for_user(user)
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response(
            {
                "message": "Login successful.",
                "tokens": tokens,
            },
            status=status.HTTP_200_OK,
        )

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers


# Создаем сериализатор для токена обновления
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True)


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    # Рекомендуется включить проверку аутентификации
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            refresh_token = serializer.validated_data['refresh']
            token = RefreshToken(refresh_token)

            # Добавляем токен в черный список
            token.blacklist()

            return Response(
                {"message": "Logout successful."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"error": f"Invalid or expired token. Details: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )



class PatientMainPageView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_queryset(self):
        return Patient.objects.filter(id=self.request.user.id)



class DoctorMainPageView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorProfileMainPageSerializer

    def get_queryset(self):
        return Doctor.objects.filter(id=self.request.user.id)


class DoctorUserProfileListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorProfileSerializer

    def get_queryset(self):
        return Doctor.objects.filter(id=self.request.user.id)

class DoctorProfileUpdateListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorProfileSerializer

    # def get_queryset(self):
    #     return Doctor.objects.filter(id=self.request.user.id)



class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ['fio']
    ordering_fields = ['price_consultation']
    filterset_class = DoctorFilter


class DoctorDetailListView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer


# Список всех слотов (свободных и занятых)
class ConsultationSlotListView(generics.ListAPIView):
    queryset = ConsultationSlot.objects.all()
    serializer_class = ConsultationSlotSerializer

# Список только доступных слотов для конкретного врача
class AvailableConsultationSlotListView(generics.ListAPIView):
    serializer_class = ConsultationSlotSerializer

    def get_queryset(self):
        doctor_id = self.request.query_params.get('doctor')
        if doctor_id:
            return ConsultationSlot.objects.filter(doctor_id=doctor_id, is_booked=False)
        return ConsultationSlot.objects.filter(is_booked=False)


# Создание нового бронирования
class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Список всех бронирований
class BookingListView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer



class FeedbackCreateViewAPI(generics.CreateAPIView):
    # queryset = Feedback.objects.all()  # queryset не нужен для create потому-что данные из базы не нужны.
    serializer_class = FeedbackCreateSerializer


class FeedbackListViewAPI(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackListCreateSerializer


    from datetime import datetime, timedelta
    from rest_framework import generics, status
    from rest_framework.response import Response
    from .models import Doctor, ConsultationSlot

    #
    # class GenerateSlotsView(generics.GenericAPIView):
    #     serializer_class = GenerateSlotsSerializer
    #
    #     def post(self, request, *args, **kwargs):
    #         serializer = self.get_serializer(data=request.data)
    #         if serializer.is_valid():
    #             doctor = serializer.validated_data['doctor_id']
    #             days_ahead = serializer.validated_data['days_ahead']
    #             slot_duration = serializer.validated_data['slot_duration']
    #
    #             # Логика генерации слотов внутри вью
    #             today = datetime.now().date()
    #             slots_to_create = []
    #
    #             for day in range(days_ahead):
    #                 consultation_date = today + timedelta(days=day)
    #                 start_time = doctor.work_start_time
    #                 end_time = doctor.work_end_time
    #
    #                 current_time = datetime.combine(consultation_date, start_time)
    #                 end_of_day = datetime.combine(consultation_date, end_time)
    #
    #                 while current_time.time() < end_of_day.time():
    #                     if not ConsultationSlot.objects.filter(doctor=doctor, date=consultation_date, time=current_time.time()).exists():
    #                         slots_to_create.append(
    #                             ConsultationSlot(doctor=doctor, date=consultation_date, time=current_time.time())
    #                         )
    #
    #                     current_time += timedelta(minutes=slot_duration)
    #
    #             if slots_to_create:
    #                 ConsultationSlot.objects.bulk_create(slots_to_create)
    #
    #             return Response({'message': 'Слоты успешно созданы!'}, status=status.HTTP_201_CREATED)
    #
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)