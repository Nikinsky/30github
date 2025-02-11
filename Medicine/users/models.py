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
    BLOOD_TYPE = (
        ('1', 'A'),
        ('2', 'B'),
        ('3', 'C'),
        ('4', 'AB'),
    )



class Doctor(UserProfile):
    fio = models.CharField(max_length=200)
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

    def __str__(self):
        return f'{self.fio} - {self.special}'

    def get_average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0



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



class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Doctor, related_name='ratings', on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], verbose_name='Рейтинг')

    def __str__(self):
        return f'{self.user} - {self.stars}'


class Feedback(models.Model): #Отзыв про специалистов
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,)
    specialist = models.ForeignKey(Doctor, related_name='reviews', on_delete=models.CASCADE)
    # parent = models.ForeignKey('self', related_name='relies', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user} - {self.specialist}'


class ConsultZapis(models.Model):
    username = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    start_con = models.DateTimeField()
    end_con = models.DateTimeField()

    def __str__(self):
        return f'{self.username} - {self.specialist}'

