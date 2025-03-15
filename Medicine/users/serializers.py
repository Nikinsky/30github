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
        fields = ['id', 'username', 'email', 'password', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Patient.objects.create_user(**validated_data)
        return user

class RegisterDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'username', 'email', 'password', 'special', 'status_edu', 'status_cat', 'phone_number']
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



# class WorkTimeSerializer(serializers.ModelSerializer):
#     start_work = serializers.TimeField(format('%H:%M'))
#     end_work = serializers.TimeField(format('%H:%M'))
#
#     class Meta:
#         model = WorkTime
#         fields = ['start_work', 'end_work']




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
    educations = EducationSerializer(many=True)
    experiences = ExperienceSerializer(many=True)
    # works_time = WorkTimeSerializer(many=True, read_only=True)
    class Meta:
        model  = Doctor
        fields = ['id', 'fio', 'special',  'about_me', 'experience', 'work_start_time', 'work_end_time', 'amount_of_consultation', 'status_edu', 'days_of_week', 'works_time', 'price_consultation', 'dlitelnost', 'educations', 'experiences',]



class DoctorListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    # works_time = WorkTimeSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ['id', 'fio', 'special', 'experience', 'work_start_time', 'work_end_time', 'average_rating', 'price_consultation', 'image', 'works_time']

    def get_average_rating(self, obj):
        return obj.get_average_rating()






class DoctorDetailSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    # ratings = FeedbackDoctorSerializer(many=True, read_only=True)
    ratings = FeedbackListCreateSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ['id', 'fio', 'special', 'about_me', 'price_consultation', 'dlitelnost', 'educations','average_rating', 'experiences', 'experience'] #rating and count consultation need add


    def get_average_rating(self, obj):
        return obj.get_average_rating()




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





class GenerateSlotsSerializer(serializers.Serializer):
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    days_ahead = serializers.IntegerField(default=14, min_value=1)
    slot_duration = serializers.IntegerField(default=30, min_value=10)


