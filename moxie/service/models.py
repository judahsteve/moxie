from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField()
    medspa = models.ForeignKey("medspa.MedSpa",on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    duration = models.IntegerField()
    
    class Meta:
        db_table = "services"
        constraints = [
            models.UniqueConstraint(fields=['name', 'medspa_id'], name='unique_medspa_services'),
        ]