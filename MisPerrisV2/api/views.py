from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from Back.models import Mascota
from . import serializers

class PerroView(APIView):
    def get(self,request):
        perros = Mascota.objects.all()
        serializer = serializers.MascotaSerializer(perros,many=True)
        return Response(serializer.data)
