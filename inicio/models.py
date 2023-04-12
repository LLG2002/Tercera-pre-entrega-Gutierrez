from django.db import models



class Clientes(models.Model):
    usuario = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=15)
    email= models.CharField(max_length=25)
    edad= models.IntegerField()
    
