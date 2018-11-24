from rest_framework import serializers
from Back.models import Mascota

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Mascota
