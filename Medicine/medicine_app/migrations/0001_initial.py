# Generated by Django 5.1.6 on 2025-02-27 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultZapis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_blue', models.CharField(max_length=300)),
                ('title_white', models.CharField(max_length=100)),
                ('older_type', models.BooleanField(default=False)),
                ('older_text', models.CharField(max_length=100)),
                ('div_title1', models.CharField(max_length=100)),
                ('des_title1', models.CharField(max_length=300)),
                ('div_title2', models.CharField(max_length=100)),
                ('des_title2', models.CharField(max_length=300)),
                ('div_title3', models.CharField(max_length=100)),
                ('des_title3', models.CharField(max_length=300)),
                ('div_title4', models.CharField(max_length=100)),
                ('des_title4', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MainPageIcons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='icons_work')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MedlinkPersonal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionsMP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', models.TextField()),
            ],
        ),
    ]
