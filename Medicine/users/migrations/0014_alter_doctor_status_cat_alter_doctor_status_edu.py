# Generated by Django 5.1.6 on 2025-02-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_rename_created_data_feedback_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='status_cat',
            field=models.CharField(choices=[('Для взрослого и ребёнка', 'Для взрослого и ребёнка'), ('Для взрослого', 'Для взрослого'), ('Для ребёнка', 'Для ребёнка')], max_length=255),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status_edu',
            field=models.CharField(choices=[('Доктор мединциских наук', 'Доктор мединциских наук'), ('Кандидат мединциских наук', 'Кандидат мединциских наук'), ('Высшее образование', 'Высшее образование')], max_length=255),
        ),
    ]
