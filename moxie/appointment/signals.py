from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from appointment.models import AppointmentService

@receiver(post_save,sender=AppointmentService)
@receiver(post_delete,sender=AppointmentService)
def updateTotalDuration(sender,instance,**kwargs):
    appointment = instance.appointment
    sums = AppointmentService.objects.filter(appointment=appointment).aggregate(
        total_duration = Sum("service__duration"),
        total_price = Sum("service__price"),
    )
    duration = sums["total_duration"]
    price = sums["total_price"]
    appointment.total_duration = duration
    appointment.total_price = price
    appointment.save()

