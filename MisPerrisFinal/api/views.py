from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vivienda
from .serializers import ViviendaSerializer
# Create your views here.
class PerroView(APIView):
    def get(self,request):
        perros=Perro.objects.all()
        serializer=PerroSerializer(viviendas,many=True)
        return Response(serializer.data)
    
class PerroFiltro(APIView):
    def get(self,request,filtro):
        perros=Perro.objects.filter(patio=filtro)
        serializer=PerroSerializer(viviendas,many=True)
        return Response(serializer.data)

    def post(self,request):
        
       return Response()
       