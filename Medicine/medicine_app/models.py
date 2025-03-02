from django.db import models
from users.models import *




class MainPage(models.Model):
    title_blue = models.CharField(max_length=300)
    title_white = models.CharField(max_length=100)
    older_type = models.BooleanField(default=False)
    older_text = models.CharField(max_length=100)


    div_title1 = models.CharField(max_length=100)
    des_title1 = models.CharField(max_length=300)
    div_title2 = models.CharField(max_length=100)
    des_title2 = models.CharField(max_length=300)
    div_title3 = models.CharField(max_length=100)
    des_title3 = models.CharField(max_length=300)
    div_title4 = models.CharField(max_length=100)
    des_title4 = models.CharField(max_length=300)



class MainPageIcons(models.Model):
    mainpage = models.ForeignKey(MainPage, related_name='icons_main', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='icons_work')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class QuestionsMP(models.Model):
    mainpage_q = models.ForeignKey(MainPage, related_name='questions_main', on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    answer = models.TextField()

    def __str__(self):
        return f'{self.question}'


class MedlinkPersonal(models.Model):
    main_page = models.ForeignKey(MainPage, related_name='personal', on_delete=models.CASCADE)
    title =models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'



# Модель слота для записи к врачу
class ConsultationSlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='slots')
    date = models.DateField()  # Дата консультации
    time = models.TimeField()  # Время консультации
    is_booked = models.BooleanField(default=False)  # Занят ли слот

    class Meta:
        unique_together = ('doctor', 'date', 'time')  # Запрещает дублирование слотов
        verbose_name = 'Consultation Slot'
        verbose_name_plural = 'Consultation Slots'

    def __str__(self):
        return f"{self.doctor} - {self.date} {self.time} {'(Занято)' if self.is_booked else '(Свободно)'}"

# Модель бронирования слота пациентом
class Booking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='bookings')
    slot = models.ForeignKey(ConsultationSlot, on_delete=models.CASCADE, related_name='bookings')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f"Бронирование {self.patient} на {self.slot}"
