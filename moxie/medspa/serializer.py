
from rest_framework import serializers
from medspa.models import Medspa
class MedspaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medspa
        fields = '__all__'
