from django.conf import settings

MAX_BOOKING_PERIOD = getattr(settings, "MAX_BOOKING_PERIOD", 30)
MIN_TIME_APPOINTMENT = getattr(settings, "MIN_TIME_APPOINTMENT", 9)
MAX_TIME_APPOINTMENT = getattr(settings, "MAX_TIME_APPOINTMENT", 18)
ACCEPTABLE_DAYS = getattr(settings, "ACCEPTABLE_DAYS", [0, 1, 2, 3, 4])
