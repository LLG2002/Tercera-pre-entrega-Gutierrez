from django.db import models



class Cliente(models.Model):
    usuario = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=15)
    
   
