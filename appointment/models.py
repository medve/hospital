from django.db import models


class Specialization(models.Model):
    """This model is used for store names of doctors' specializations."""
    name = models.CharField(max_length=30, unique=True,
                            verbose_name=u"Название специализации")

    def __str__(self):
        return self.name


class Doctor(models.Model):
    """
    This models is used for store info about every doctor.

    Field "name" contains full name of the doctor.

    Field "specialization" contains info about professional field of this
    doctor. Say every doctor has only one specialization.


    """
    available = models.BooleanField(default=True, db_index=True,
                                    verbose_name=u"Доступен")
    name = models.CharField(max_length=100, verbose_name=u"Имя доктора")
    specialization = models.ForeignKey(Specialization,
                                       verbose_name=u"Специализация")

    def __str__(self):
        return u"%s(%s)" % (self.name, self.specialization)


class Appointment(models.Model):
    """(Appointment description)"""
    doctor = models.ForeignKey(Doctor, verbose_name=u"Доктор")
    appointment_time = models.DateTimeField(verbose_name=u"Время приема",
                                            unique=True,
                                            db_index=True)
    patient = models.CharField(max_length=100, verbose_name=u"Имя пациента")

    def __str__(self):
        return u"[%s] %s к %s" % (
                 self.appointment_time.strftime("%a %d %b %Y %H:%M"),
                 self.doctor, self.appointment_time)
