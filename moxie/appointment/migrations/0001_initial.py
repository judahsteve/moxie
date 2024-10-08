# Generated by Django 5.1 on 2024-08-29 02:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("medspa", "0001_initial"),
        ("service", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateField()),
                ("start_time", models.TimeField()),
                ("total_duration", models.IntegerField()),
                ("total_price", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("scheduled", "Scheduled"),
                            ("completed", "Completed"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="scheduled",
                    ),
                ),
                (
                    "med_spa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="medspa.medspa"
                    ),
                ),
            ],
            options={
                "db_table": "appointments",
            },
        ),
        migrations.CreateModel(
            name="AppointmentService",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "appointment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appointment.appointment",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="service.service",
                    ),
                ),
            ],
            options={
                "db_table": "appointment_services",
            },
        ),
    ]
