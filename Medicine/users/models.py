from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class SpecialDoctor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'



class UserProfile(AbstractUser):
    pass


class Patient(UserProfile):
    fio = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(default=1)
    phone_number = PhoneNumberField(null=True, blank=True, region="KG")
    image = models.ImageField(upload_to='patient_img', null=True, blank=True)
    BLOOD_TYPE = (
        ('1', 'A'),
        ('2', 'B'),
        ('3', 'C'),
        ('4', 'AB'),
    )

    class Meta:
        verbose_name_plural = "Patient"


class Doctor(UserProfile):
    fio = models.CharField(max_length=200)
    image = models.ImageField(upload_to='doctor_img', null=True, blank=True)
    special = models.ForeignKey(SpecialDoctor, related_name='special_doctor', on_delete=models.CASCADE)
    about_me = models.TextField(null=True, blank=True)
    experience = models.PositiveSmallIntegerField([MinValueValidator(1), MaxValueValidator(70)])
    amount_of_consultation = models.CharField(max_length=100)
    EDU_CHOICES = {
        ('Высшее образование', 'Высшее образование'),
        ('Кандидат мединциских наук', 'Кандидат мединциских наук'),
        ('Доктор мединциских наук', 'Доктор мединциских наук')
    }
    status_edu = models.CharField(max_length=255, choices=EDU_CHOICES)

    CAT_CHOICES = {
        ('Для взрослого', 'Для взрослого'),
        ('Для ребёнка', 'Для ребёнка'),
        ('Для взрослого и ребёнка', 'Для взрослого и ребёнка'),
    }
    status_cat = models.CharField(max_length=255, choices=CAT_CHOICES)

    DAYS_OF_WEEK = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('San', 'Sunday'),
    ]
    days_of_week = MultiSelectField(choices=DAYS_OF_WEEK, max_choices=5, max_length=100)  # Allow selecting 3 days
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



class WorkTime(models.Model):
    start_work = models.TimeField()
    end_work = models.TimeField()
    doctor = models.ForeignKey(Doctor, related_name='works_time', on_delete=models.CASCADE)



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





class Feedback(models.Model): #Отзыв про специалистов
    user = models.ForeignKey(Patient, related_name='feedbacks_user', on_delete=models.CASCADE,)
    specialist = models.ForeignKey(Doctor, related_name='ratings', on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], verbose_name='Рейтинг')
    # parent = models.ForeignKey('self', related_name='relies', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user} - {self.specialist}'