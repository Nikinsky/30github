from rest_framework import serializers
from .models import *



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

class DoctorProfileSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True)
    experiences = ExperienceSerializer(many=True)
    ratings = FeedbackDoctorSerializer(many=True, read_only=True)
    class Meta:
        model  = Doctor
        fields = ['id', 'fio', 'special', 'educations', 'ratings', 'experiences', 'about_me', 'experience', 'amount_of_consultation', 'status_edu', 'days_of_week',]


class DoctorListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'fio', 'special', 'experience',]


class DoctorDetailSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    ratings = FeedbackDoctorSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'fio', 'special', 'educations', 'ratings','average_rating', 'experiences', 'about_me','experience'] #rating and count consultation need add


    def get_average_rating(self, obj):
        return obj.get_average_rating()


class FeedbackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'specialist', 'stars', 'text','created_date']



