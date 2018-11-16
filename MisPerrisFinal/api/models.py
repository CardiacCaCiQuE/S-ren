from django.db import models

# Create your models here.
class Perro(models.Model):
    nombrePerro=models.Charfield(max_length=20)
    razaPerro=models.Charfield(max_length=50)
    descPerro=models.Charfield(max_length=250)
    estadoPerro=models.Charfield(max_length=15)
