from django.db import models



class Clientes(models.Model):
    usuario = models.CharField(max_length=15)
    conjunto = models.IntegerField() 
    producto = models.CharField(max_length=15) 
    email= models.CharField(max_length=25)
    telefono= models.IntegerField()
    
