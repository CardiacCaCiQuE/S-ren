from django.db import models #importacion de la libreria models
from django.contrib.auth.models import User # importacion de la libreria user para generacion de usuarioas
# Create your models here.

#Creacion de usuarios personalizados
# Con los diferentes campos

class Usuario(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    perfil=models.CharField(max_length=20,default="Usuario")
#Creacion de la clase mascota
class Mascota(models.Model):
    codigoMascota=models.AutoField(primary_key=True)
    fotoMascota=models.ImageField(upload_to='Back/static/media/')# donde se guaradaran las imagenes
    nombreMascota=models.CharField(max_length=20)
    razaMascota=models.CharField(max_length=30)
    descripcionMascota=models.TextField(max_length=250)
    estadoMascota=models.CharField(max_length=20,default="Rescatado")
# Creacion de la clase mensaje
class Mensaje(models.Model):
    codigo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=20)
    correo=models.CharField(max_length=20,null=True,blank=True)
    mensaje=models.TextField(max_length=200)