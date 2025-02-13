from django.urls import path, include
from .views import *

urlpatterns = [
    path('main_page', MainPageListView.as_view(), name='main_page-list'),


]