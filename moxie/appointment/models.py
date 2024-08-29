from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class Appointment(models.Model):
    medspa = models.ForeignKey("medspa.MedSpa",on_delete=models.CASCADE)
    start_date = models.DateField()
    start_time = models.TimeField()
    total_duration = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    status = models.CharField(choices=[("scheduled","Scheduled"),("completed","Completed"),("cancelled","Cancelled")],default="scheduled")

    class Meta:
        db_table = "appointments"

class AppointmentService(models.Model):
    appointment = models.ForeignKey("appointment.Appointment",on_delete=models.CASCADE)
    service = models.ForeignKey("service.Service",on_delete=models.CASCADE)

    class Meta:
        db_table = "appointment_services"