from django_filters import FilterSet
from .models import *

class DoctorFilter(FilterSet):
    class Meta:
        model = Doctor
        fields = {
            'special':['exact'],
            'status_cat': ['exact'],
            'status_edu': ['exact'],

        }