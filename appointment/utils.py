from django.conf import settings
from pytz import timezone

from .models import Appointment
from .settings import *

TIME_ZONE = getattr(settings, 'TIME_ZONE', 'UTC')

def get_free_time(doctor_id, appointment_date):
    """Returns list of free hours of doctor for some date"""
    appointments = Appointment.objects.filter(
                                doctor_id=doctor_id,
                                appointment_time__year=appointment_date.year,
                                appointment_time__month=appointment_date.month,
                                appointment_time__day=appointment_date.day)
    cur_tz = timezone(TIME_ZONE)
    reserved_hours = {x.appointment_time.astimezone(cur_tz).hour
                      for x in appointments}
    times = [x for x in range(MIN_TIME_APPOINTMENT, MAX_TIME_APPOINTMENT)
             if x not in reserved_hours]
    return times
