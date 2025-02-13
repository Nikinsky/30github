from rest_framework import serializers
from .models import *



class MPIconsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageIcons
        fields = ['id', 'img', 'name']


class MPQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageIcons
        fields = ['id', 'question', 'answer']


class MedlinkPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageIcons
        fields = ['id', 'title']



class MainPageSerializer(serializers.ModelSerializer):
    icons_main = MPIconsSerializer(many=True)
    questions_main = MPQuestionsSerializer(many=True)
    personal = MedlinkPersonalSerializer(many=True)
    class Meta:
        model = MainPage
        fields = ['title_blue', 'title_white', 'older_type', 'older_text', 'icons_main', 'questions_main', 'personal',
                  'div_title1', 'des_title1',
                  'div_title2', 'des_title2',
                  'div_title3', 'des_title3',
                  'div_title4', 'des_title4',
                  ]





