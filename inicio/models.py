from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Clientes(models.Model):
    usuario = models.CharField(max_length=15)
    conjunto = models.IntegerField() 
    producto = models.CharField(max_length=15)
    descripcion = RichTextField(null=True) 
    email= models.CharField(max_length=25, default='ejemplo@gmail.com')
    telefono= models.IntegerField(null=True)
    fecha_de_realizacion = models.DateField(default=timezone.now)
    imagen = models.ImageField(upload_to='clientes/', null=True)
    
