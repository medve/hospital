from datetime import datetime

import django.forms as forms

from .models import Appointment, Doctor
from .settings import *
from .utils import get_free_time
from .validators import *


def get_dates():
    today = date.today()
    dates = [(None, "Выберите дату")]
    for x in range(1, MAX_BOOKING_PERIOD + 1):
        new_date = today + timedelta(days=x)
        if date_is_acceptable(new_date):
            dates.append((new_date.toordinal(),
                          new_date.strftime("%a %d %b")))
    return dates


def coerce_date(raw_date):
    data = raw_date
    try:
        ordinal_date = int(data)
        coerced_date = date.fromordinal(ordinal_date)
    except ValueError:
        raise forms.ValidationError("Bad date value")
    if not date_is_acceptable(coerced_date):
        raise forms.ValidationError("Date is not acceptable")
    if not date_in_range(coerced_date):
        raise forms.ValidationError("Date range is not acceptable")
    return coerced_date


def coerce_hour(hour):
    data = hour
    try:
        data = int(data)
    except ValueError:
        raise forms.ValidationError("Bad time value")
    if not time_in_range(data):
        raise forms.ValidationError("Bad time range")
    return data


class AppointmentForm(forms.ModelForm):

    doctor = forms.ModelChoiceField(
               queryset=Doctor.objects.filter(available=True).select_related(),
               required=True,
               label="Доктор")
    appointment_date = forms.TypedChoiceField(choices=get_dates,
                                              empty_value=None,
                                              coerce=coerce_date,
                                              label="Дата приема")
    appointment_hour = forms.TypedChoiceField(
                         choices=[(None, "Выберите время")]+
                         [(x, x) for x in range(MIN_TIME_APPOINTMENT,
                          MAX_TIME_APPOINTMENT)],
                         empty_value=None,
                         coerce=coerce_hour,
                         label="Время приема")
    patient = forms.CharField(label="Ваше ФИО")

    def clear(self, *args, **kwargs):
        cleaned_data = super(AppointmentForm,self).clear(*args,**kwargs)
        adate = cleaned_data['appointment_date']
        ahour = cleaned_data['appointment_hour']
        doctor = cleaned_data['doctor']
        if ahour not in get_free_time(doctor, adate):
            raise ValidationError("Time is reserved")
        return cleaned_data



    def save(self, *args, **kwargs):
        inst = super(AppointmentForm, self).save(commit=False, *args, **kwargs)
        adate = self.cleaned_data['appointment_date']
        ahour = self.cleaned_data['appointment_hour']
        commit = kwargs.pop('commit', True)
        inst.appointment_time = datetime(day=adate.day,
                                         month=adate.month,
                                         year=adate.year,
                                         hour=ahour)
        if commit:
            inst.save()
        return inst

    class Meta:
        model = Appointment
        fields = ['doctor', 'appointment_date', 'appointment_hour', 'patient']

    class Media:
        js = ['js/jquery.min.js', 'js/form.js']
