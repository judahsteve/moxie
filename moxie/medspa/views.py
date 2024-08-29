from django.shortcuts import render
from rest_framework import viewsets
from medspa.models import Medspa
from medspa.serializer import MedspaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# Create your views here.
class MedspaViewSet(viewsets.ModelViewSet):
    """
    list: Return a list of Medspa
    """
    queryset = Medspa.objects.all()
    serializer_class = MedspaSerializer
    renderer_classes = [JSONRenderer]

    def getMedspas(self,  request, product_id):
        """
        Gets all medspas
        """
        # TODO: place the code here
        product_category = ProductCategory.objects.filter(product_id=product_id)
        category_id = product_category[0].category_id if product_category else -1
        queryset = self.queryset.filter(pk=category_id)
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data) 