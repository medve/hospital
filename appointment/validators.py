from datetime import date, timedelta

from .settings import *


def date_is_acceptable(d_check):
    """Date range validation"""
    return d_check.weekday() in ACCEPTABLE_DAYS

def date_in_range(d_check):
    """Date range validation"""
    return (d_check <= d_check + timedelta(days=MAX_BOOKING_PERIOD) and
            d_check > date.today())

def time_in_range(t_check):
    """Time range validation"""
    return t_check in range(MIN_TIME_APPOINTMENT, MAX_TIME_APPOINTMENT)
