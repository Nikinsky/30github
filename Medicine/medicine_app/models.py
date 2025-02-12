from django.db import models
from users.models import *

class MainPage(models.Model):
    title_blue = models.CharField(max_length=300)
    title_white = models.CharField(max_length=100)
    older_tupe = models.BooleanField(default=False)
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



class ConsultZapis(models.Model):
    username = models.ForeignKey(Patient, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    start_con = models.DateTimeField()
    end_con = models.DateTimeField()

    def __str__(self):
        return f'{self.username} - {self.specialist}'
