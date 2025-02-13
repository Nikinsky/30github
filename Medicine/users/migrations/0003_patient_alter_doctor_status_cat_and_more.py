# Generated by Django 5.1.6 on 2025-02-12 17:17

import django.contrib.auth.models
import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_bio_doctor_about_me_alter_doctor_experience_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fio', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField(default=1)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.userprofile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status_cat',
            field=models.CharField(choices=[('Для взрослого', 'Для взрослого'), ('Для ребёнка', 'Для ребёнка'), ('Для взрослого и ребёнка', 'Для взрослого и ребёнка')], max_length=255),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status_edu',
            field=models.CharField(choices=[('Высшее образование', 'Высшее образование'), ('Кандидат мединциских наук', 'Кандидат мединциских наук'), ('Доктор мединциских наук', 'Доктор мединциских наук')], max_length=255),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='users.doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks_user', to='users.patient')),
            ],
        ),
        migrations.CreateModel(
            name='ConsultZapis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_con', models.DateTimeField()),
                ('end_con', models.DateTimeField()),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.doctor')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Рейтинг')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='users.doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_user', to='users.patient')),
            ],
        ),
    ]
