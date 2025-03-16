from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

MEDICAL_SPECIALTIES = [
    ('therapist', 'Терапевт'),
    ('family_doctor', 'Семейный врач'),
    ('pediatrician', 'Педиатр'),
    ('surgeon', 'Хирург'),
    ('traumatologist', 'Травматолог-ортопед'),
    ('neurologist', 'Невролог'),
    ('cardiologist', 'Кардиолог'),
    ('pulmonologist', 'Пульмонолог'),
    ('gastroenterologist', 'Гастроэнтеролог'),
    ('endocrinologist', 'Эндокринолог'),
    ('nephrologist', 'Нефролог'),
    ('hematologist', 'Гематолог'),
    ('rheumatologist', 'Ревматолог'),
    ('infectiologist', 'Инфекционист'),
    ('allergist', 'Аллерголог-иммунолог'),
    ('gynecologist', 'Гинеколог'),
    ('obstetrician', 'Акушер'),
    ('urologist', 'Уролог'),
    ('andrologist', 'Андролог'),
    ('radiologist', 'Рентгенолог'),
    ('ultrasound_diagnostician', 'УЗИ-диагност'),
    ('psychiatrist', 'Психиатр'),
    ('psychotherapist', 'Психотерапевт'),
    ('clinical_psychologist', 'Клинический психолог'),
    ('ophthalmologist', 'Офтальмолог'),
    ('otolaryngologist', 'Оториноларинголог (ЛОР)'),
    ('dermatologist', 'Дерматолог'),
    ('dentist', 'Стоматолог'),
    ('neonatologist', 'Неонатолог'),
    ('physiotherapist', 'Физиотерапевт'),
    ('speech_therapist', 'Логопед'),
]

class UserProfile(AbstractUser):
    pass


class Patient(UserProfile):
    fio = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(default=1)
    phone_number = PhoneNumberField(null=True, blank=True, region="KG")
    image = models.ImageField(upload_to='patient_img', null=True, blank=True)


    class Meta:
        verbose_name_plural = "Patient"


class Doctor(UserProfile):
    fio = models.CharField(max_length=200)
    image = models.ImageField(upload_to='doctor_img', null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, region="KG")
    about_me = models.TextField(null=True, blank=True)
    experience = models.PositiveSmallIntegerField([MinValueValidator(1), MaxValueValidator(70)], null=True, blank=True)
    amount_of_consultation = models.CharField(max_length=100)
    work_start_time = models.TimeField(default='09:00')  # Начало рабочего дня
    work_end_time = models.TimeField(default='17:00')    # Конец рабочего дня
    telegram_link = models.URLField(null=True, blank=True)
    whatsapp_link = models.URLField(null=True, blank=True)
    EDU_CHOICES = {
        ('Высшее образование', 'Высшее образование'),
        ('Кандидат мединциских наук', 'Кандидат мединциских наук'),
        ('Доктор мединциских наук', 'Доктор мединциских наук')
    }
    status_edu = models.CharField(max_length=255, choices=EDU_CHOICES, null=True, blank=True)
    medicine_special = models.CharField(max_length=255, choices=MEDICAL_SPECIALTIES, null=True, blank=True)


    CAT_CHOICES = {
        ('Для взрослого', 'Для взрослого'),
        ('Для ребёнка', 'Для ребёнка'),
        ('Для взрослого и ребёнка', 'Для взрослого и ребёнка'),
    }
    status_cat = models.CharField(max_length=255, choices=CAT_CHOICES, null=True, blank=True)

    DAYS_OF_WEEK = [
        ('Mon', 'Понедельник'),
        ('Tue', 'Вторник'),
        ('Wed', 'Среда'),
        ('Thu', 'Четверг'),
        ('Fri', 'Пятница'),
        ('Sat', 'Суббота'),
        ('Sun', 'Воскресенье'),
    ]
    days_of_week = MultiSelectField(choices=DAYS_OF_WEEK, max_choices=7, max_length=100)  # Allow selecting 3 days
    price_consultation = models.PositiveSmallIntegerField(default=1000, null=True, blank=True)
    dlitelnost = models.CharField(max_length=100, default='60 мин.', help_text="Длительность")

    class Meta:
        verbose_name_plural = "Doctor"


    def __str__(self):
        return f'{self.fio} - {self.special}'

    def get_average_rating(self):
        rating = self.ratings.all()
        if rating.exists():
            return (round(sum(rating.stars for rating in rating) / rating.count(), 1))
        return 0


#
# class WorkTime(models.Model):
#     start_work = models.TimeField()
#     end_work = models.TimeField()
#     doctor = models.ForeignKey(Doctor, related_name='works_time', on_delete=models.CASCADE)
#


class Education(models.Model):
    specialist_educations = models.ForeignKey(Doctor, related_name='educations', on_delete=models.CASCADE)
    # during_education = DateRangeField()
    start_edu = models.DateField()
    end_edu = models.DateField()
    description_study = models.TextField()

    def __str__(self):
        return f'{self.specialist_educations} - {self.start_edu} - {self.end_edu}'


class Experience(models.Model):
    specialist_experience = models.ForeignKey(Doctor, related_name='experiences', on_delete=models.CASCADE)
    # during_education = DateRangeField()
    start_exper = models.DateField()
    end_exper = models.DateField()
    description_exper = models.TextField()

    def __str__(self):
        return f'{self.specialist_experience} - {self.start_exper} - {self.end_exper}'


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
        unique_together = ('patient', 'slot')  # Запрещает дублирование слотов
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f"Бронирование {self.patient} на {self.slot}"



class Feedback(models.Model): #Отзыв про специалистов
    user = models.ForeignKey(Patient, related_name='feedbacks_user', on_delete=models.CASCADE,)
    specialist = models.ForeignKey(Doctor, related_name='ratings', on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], verbose_name='Рейтинг')
    # parent = models.ForeignKey('self', related_name='relies', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user} - {self.specialist}'