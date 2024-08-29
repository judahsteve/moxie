from django.shortcuts import render
from rest_framework import viewsets
from service.models import Service
from service.serializer import ServiceSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):
   
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    renderer_classes = [JSONRenderer]


    def get_by_medspa(self, request,  medspa):
        options = ["scheduled","completed","cancelled"]
        if not medspa:
            return Response({'error': 'Invalid input please input correct medspa id'}, status=400)
        appointments = Service.objects.filter(medspa_id=medspa)
        return Response(self.serializer_class(appointments,many=True).data)
    
    def update(self, request, *args, **kwargs):
        
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            name = request.data.get('name', '')
            description = request.data.get('description', '')
            price = int(request.data.get('price', ''))
            duration = request.data.get('duration', '')
            instance.name = name
            instance.description = description
            instance.price = price
            instance.duration = duration
            instance.save()
        else:
            return Response({'error': 'Invalid input please input correct values'}, status=400)
     
        
        
        return Response(self.serializer_class(instance).data)