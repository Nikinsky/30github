# Generated by Django 5.1.6 on 2025-03-15 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_doctor_status_cat_alter_doctor_status_edu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='status_cat',
            field=models.CharField(blank=True, choices=[('Для ребёнка', 'Для ребёнка'), ('Для взрослого', 'Для взрослого'), ('Для взрослого и ребёнка', 'Для взрослого и ребёнка')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status_edu',
            field=models.CharField(blank=True, choices=[('Доктор мединциских наук', 'Доктор мединциских наук'), ('Высшее образование', 'Высшее образование'), ('Кандидат мединциских наук', 'Кандидат мединциских наук')], max_length=255, null=True),
        ),
    ]
