from datetime import datetime, timedelta, time
from django.utils import timezone
from .models import *


def generate_consultation_slots(doctor: Doctor, days_ahead: int = 7, slot_duration: int = 30):
    """
    Автоматическая генерация слотов для врача на указанный период.
    :param doctor: Доктор, для которого создаются слоты
    :param days_ahead: На сколько дней вперёд генерировать слоты (по умолчанию 7 дней)
    :param slot_duration: Длительность одного слота в минутах (по умолчанию 30 минут)
    """
    today = timezone.now().date()
    work_start = doctor.work_start_time
    work_end = doctor.work_end_time

    # Переводим дни недели из MultiSelectField в список
    work_days = [day for day, _ in Doctor.DAYS_OF_WEEK if day in doctor.days_of_week]

    for day_offset in range(days_ahead):
        slot_date = today + timedelta(days=day_offset)
        weekday = slot_date.strftime('%a')  # Получаем короткое название дня недели (например, 'Mon')

        if weekday not in work_days:
            continue  # Пропускаем дни, когда врач не работает

        # Генерация временных слотов
        current_time = datetime.combine(slot_date, work_start)
        end_time = datetime.combine(slot_date, work_end)

        while current_time < end_time:
            slot_time = current_time.time()

            # Проверка на существование слота (чтобы не дублировать)
            if not ConsultationSlot.objects.filter(doctor=doctor, date=slot_date, time=slot_time).exists():
                ConsultationSlot.objects.create(
                    doctor=doctor,
                    date=slot_date,
                    time=slot_time,
                    is_booked=False
                )
            current_time += timedelta(minutes=slot_duration)
