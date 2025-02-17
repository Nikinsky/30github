from rest_framework import generics, viewsets
from .serializers import *


class MainPageListView(generics.ListAPIView):
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer

