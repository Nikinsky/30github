# Generated by Django 5.1.6 on 2025-03-14 16:15

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SpecialDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fio', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='doctor_img')),
                ('about_me', models.TextField(blank=True, null=True)),
                ('experience', models.PositiveSmallIntegerField(verbose_name=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(70)])),
                ('amount_of_consultation', models.CharField(max_length=100)),
                ('work_start_time', models.TimeField(default='09:00')),
                ('work_end_time', models.TimeField(default='17:00')),
                ('status_edu', models.CharField(choices=[('Доктор мединциских наук', 'Доктор мединциских наук'), ('Кандидат мединциских наук', 'Кандидат мединциских наук'), ('Высшее образование', 'Высшее образование')], max_length=255)),
                ('status_cat', models.CharField(choices=[('Для ребёнка', 'Для ребёнка'), ('Для взрослого', 'Для взрослого'), ('Для взрослого и ребёнка', 'Для взрослого и ребёнка')], max_length=255)),
                ('days_of_week', multiselectfield.db.fields.MultiSelectField(choices=[('Mon', 'Понедельник'), ('Tue', 'Вторник'), ('Wed', 'Среда'), ('Thu', 'Четверг'), ('Fri', 'Пятница'), ('Sat', 'Суббота'), ('Sun', 'Воскресенье')], max_length=100)),
                ('price_consultation', models.PositiveSmallIntegerField(blank=True, default=1000, null=True)),
                ('dlitelnost', models.CharField(default='60 мин.', help_text='Длительность', max_length=100)),
                ('special', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_doctor', to='users.specialdoctor')),
            ],
            options={
                'verbose_name_plural': 'Doctor',
            },
            bases=('users.userprofile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fio', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField(default=1)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG')),
                ('image', models.ImageField(blank=True, null=True, upload_to='patient_img')),
            ],
            options={
                'verbose_name_plural': 'Patient',
            },
            bases=('users.userprofile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_exper', models.DateField()),
                ('end_exper', models.DateField()),
                ('description_exper', models.TextField()),
                ('specialist_experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='users.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_edu', models.DateField()),
                ('end_edu', models.DateField()),
                ('description_study', models.TextField()),
                ('specialist_educations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='users.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='ConsultationSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('is_booked', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='users.doctor')),
            ],
            options={
                'verbose_name': 'Consultation Slot',
                'verbose_name_plural': 'Consultation Slots',
                'unique_together': {('doctor', 'date', 'time')},
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Рейтинг')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='users.doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks_user', to='users.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='users.consultationslot')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='users.patient')),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
                'unique_together': {('patient', 'slot')},
            },
        ),
    ]
