# Generated by Django 5.1.6 on 2025-02-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_categoryconsultation_alter_doctor_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='status_edu',
            field=models.CharField(choices=[('Доктор мединциских наук', 'Доктор мединциских наук'), ('Кандидат мединциских наук', 'Кандидат мединциских наук'), ('Высшее образование', 'Высшее образование')], max_length=255),
        ),
    ]
