from datetime import date, timedelta

from django.http import (HttpResponseBadRequest, HttpResponseRedirect,
                         JsonResponse)
from django.shortcuts import render

from .forms import AppointmentForm
from .models import Appointment, Doctor
from .settings import *
from .utils import get_free_time


def get_free_time_view(request):
    if not ("doctor" in request.GET.keys() and
            "appointment_date" in request.GET.keys()):
        return HttpResponseBadRequest(
                "Doctor's id or date of appointment is not set")
    try:
        ordinal_date = int(request.GET["appointment_date"])
        appointment_date = date.fromordinal(ordinal_date)
    except ValueError:
        return HttpResponseBadRequest("Bad appointment date value")
    try:
        doctor_id = int(request.GET["doctor"])
    except ValueError:
        return HttpResponseBadRequest("Bad doctor's id value")
    return JsonResponse({"times": get_free_time(doctor_id, appointment_date)})


def start_page(request, template_name):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = AppointmentForm()
    return render(request, template_name, context={"form": form})
