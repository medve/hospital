# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('appointment_time', models.DateTimeField(db_index=True, verbose_name='Время приема', unique=True)),
                ('patient', models.CharField(verbose_name='Имя пациента', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('available', models.BooleanField(db_index=True, verbose_name='Доступен', default=True)),
                ('name', models.CharField(verbose_name='Имя доктора', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Название специализации', unique=True, max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialization',
            field=models.ForeignKey(verbose_name='Специализация', to='appointment.Specialization'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(verbose_name='Доктор', to='appointment.Doctor'),
        ),
    ]
