from rest_framework import serializers
from .models import *



class MPIconsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageIcons
        fields = ['id', 'img', 'name']


class MPQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsMP
        fields = ['id', 'question', 'answer']


class MedlinkPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedlinkPersonal
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



