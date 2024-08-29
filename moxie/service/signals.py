from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from service.models import Service
from appointment.models import Appointment,AppointmentService

@receiver(post_save,sender=Service)
@receiver(post_delete,sender=Service)
def updateTotalDuration(sender,instance,**kwargs):
    medspa = instance.medspa
    appointments = Appointment.objects.filter(medspa=medspa)
    for appointment in appointments:
        sums = AppointmentService.objects.filter(appointment=appointment).aggregate(
            total_duration = Sum("service__duration"),
            total_price = Sum("service__price")
        )
        duration = sums["total_duration"]
        price = sums["total_price"]
        appointment.total_duration = duration
        appointment.total_price = price
        appointment.save()

