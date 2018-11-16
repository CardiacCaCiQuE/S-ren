from rest_framework import serializers
from .models import Perro
class PerroSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            '__all__'
        )
        model=Perro
    