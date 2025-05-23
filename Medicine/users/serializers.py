from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .models import *



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class RegisterPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'username', 'fio',  'email', 'password', 'phone_number', 'image']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Patient.objects.create_user(**validated_data)
        return user

class RegisterDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'username', 'fio', 'email', 'password', 'medicine_special', 'status_edu', 'status_cat', 'phone_number', 'image']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Doctor.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)





class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'fio', 'image',]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'start_edu', 'end_edu', 'description_study']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'start_exper', 'end_exper', 'description_exper']


class FeedbackListSerializer(serializers.ModelSerializer):
    user = PatientSerializer
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'stars', 'text', 'created_date']


class FeedbackDoctorSerializer(serializers.ModelSerializer):
    user = PatientSerializer()
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'stars', 'text', 'created_date']


class FeedbackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'specialist', 'stars', 'text','created_date']


class FeedbackListCreateSerializer(serializers.ModelSerializer):
    user = PatientSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = ['id', 'user', 'stars', 'text', 'created_date']



class DoctorProfileSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    # works_time = WorkTimeSerializer(many=True, read_only=True)
    class Meta:
        model  = Doctor
        fields = ['id', 'fio', 'medicine_special',  'image', 'about_me', 'experience', 'work_start_time', 'work_end_time', 'amount_of_consultation', 'status_edu', 'price_consultation', 'dlitelnost', 'educations', 'experiences', 'telegram_link', 'whatsapp_link']



class DoctorProfileMainPageSerializer(serializers.ModelSerializer):
    # works_time = WorkTimeSerializer(many=True, read_only=True)
    class Meta:
        model  = Doctor
        fields = ['id', 'fio', 'image']



class DoctorListSerializer(serializers.ModelSerializer):
    # average_rating = serializers.SerializerMethodField()
    # works_time = WorkTimeSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ['id', 'fio', 'medicine_special', 'experience', 'work_start_time', 'price_consultation', 'image']






class DoctorDetailSerializer(serializers.ModelSerializer):
    educations = EducationSerializer()
    experiences = ExperienceSerializer()
    ratings =  FeedbackListCreateSerializer(many=True, read_only=True)
    # average_rating = serializers.SerializerMethodField()
    # ratings = FeedbackDoctorSerializer(many=True, read_only=True)
    # ratings = FeedbackListCreateSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ['id', 'fio', 'medicine_special', 'image', 'about_me', 'price_consultation', 'dlitelnost', 'educations', 'experiences', 'experience', 'whatsapp_link', 'telegram_link','ratings'] #rating and count consultation need add


    # def get_average_rating(self, obj):
    #     return obj.get_average_rating()




# Сериализатор для слотов консультаций
class ConsultationSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationSlot
        fields = ['id', 'doctor', 'date', 'time', 'is_booked']

# Сериализатор для бронирования слотов
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'patient', 'slot']

    def validate(self, data):
        slot = data.get('slot')
        if slot.is_booked:
            raise serializers.ValidationError("Слот уже забронирован.")
        return data

    def create(self, validated_data):
        slot = validated_data['slot']
        slot.is_booked = True
        slot.save()
        return super().create(validated_data)


