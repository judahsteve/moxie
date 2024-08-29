from django.shortcuts import render
from rest_framework import viewsets
from appointment.models import Appointment,AppointmentService
from medspa.models import Medspa
from service.models import Service
from appointment.serializer import AppointmentSerializer, AppointmentServiceSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    renderer_classes = [JSONRenderer]

    def create(self, request, *args, **kwargs):
        # Custom create logic goes here
        start_date = request.data.get('start_date', '')
        start_time = request.data.get('start_time', '')
        medspa_id = int(request.data.get('medspa', ''))
        services = request.data.get('services', [])
        
        if not start_date or not start_time or not medspa_id or not services:
            return Response({'error': 'Missing required fields'}, status=400)

        try:
            medspa = Medspa.objects.get(pk=medspa_id)
        except Medspa.DoesNotExist:
            return Response({'error': 'Medspa not found'}, status=404)
        
        #confirm that all services belong to the medspa before continuing
        for service in services:
            service_ = Service.objects.filter(name=service,medspa_id=medspa.pk).first()
            if not service_:
                return Response({'error': 'Invalid services specified for medspa'}, status=404)

        appointment= Appointment(start_date=start_date,start_time=start_time,medspa=medspa)
        appointment.save()
        
        for service in services:
            service_ = Service.objects.filter(name=service,medspa_id=medspa.pk).first()
            if service_:
                appointment_service = AppointmentService(appointment_id=appointment.id,service=service_)
                appointment_service.save()
        updated_appointment = Appointment.objects.get(pk=appointment.pk)
        return Response(self.serializer_class(updated_appointment).data)
    
    def update(self, request, *args, **kwargs):
        
        instance = self.get_object()
        status = request.data.get('status', '')
        options = ["scheduled","completed","cancelled"]
        
        if not status or status not in options:
            return Response({'error': 'Invalid input please input correct status'}, status=400)
        instance = self.get_object()
        instance.status = status
        instance.save()
        return Response(self.serializer_class(instance).data)
    
    
    def get_by_status(self, request,  status):
        options = ["scheduled","completed","cancelled"]
        if not status or status not in options:
            return Response({'error': 'Invalid input please input correct status'}, status=400)
        appointments = Appointment.objects.filter(status=status)
        return Response(self.serializer_class(appointments,many=True).data)
    

    def get_by_start_date(self, request,  start_date):
        if not start_date:
            return Response({'error': 'Invalid input please input correct status'}, status=400)
        appointments = Appointment.objects.filter(start_date=start_date)
        return Response(self.serializer_class(appointments,many=True).data)