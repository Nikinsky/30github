from django.db import models


class MainPage(models.Model):
    title = models.CharField(max_length=300)

    div_tile1 = models.CharField(max_length=100)
    des_title1 = models.CharField(max_length=300)
    div_tile2 = models.CharField(max_length=100)
    des_title2 = models.CharField(max_length=300)
    div_tile3 = models.CharField(max_length=100)
    des_title3 = models.CharField(max_length=300)
    div_tile4 = models.CharField(max_length=100)
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

