from rest_framework import viewsets, generics
from .serializers import *

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
    serializer_class = DoctorProfileSerializer

