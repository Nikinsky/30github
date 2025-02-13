from rest_framework import serializers
from .models import *



class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Doctor
        fields = ['id', 'fio', 'special', 'about_me', 'experience', 'amount_of_consultation', 'status_edu', 'days_of_week',]


class DoctorListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'fio', 'special', 'experience',]


class DoctorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'fio', 'special', 'about_me', 'experience',] #rating and count consultation need add