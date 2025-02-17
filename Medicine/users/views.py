from rest_framework import generics, viewsets, status, permissions
from .serializers import *
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth.models import update_last_login
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from django.contrib.auth import authenticate


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


class LoginView(generics.GenericAPIView):
    """Авторизация пользователя по email с выдачей токенов"""
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {"error": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = Patient.objects.get(email=username)
        except Patient.DoesNotExist:
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
    """Логаут пользователя"""
    serializer_class = LogoutSerializer

    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            # Валидируем входные данные через сериализатор
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            refresh_token = serializer.validated_data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "Logout successful."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"error": "Invalid or expired token."},
                status=status.HTTP_400_BAD_REQUEST,
            )

class DoctorUserProfileListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorProfileSerializer

    def get_queryset(self):
        return Doctor.objects.filter(id==self.request.user.id)


class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorProfileSerializer



class DoctorDetailListView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer



class FeedbackCreateViewAPI(generics.CreateAPIView):
    # queryset = Feedback.objects.all()  # queryset не нужен для create потому-что данные из базы не нужны.
    serializer_class = FeedbackCreateSerializer


class FeedbackListViewAPI(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackListCreateSerializer

