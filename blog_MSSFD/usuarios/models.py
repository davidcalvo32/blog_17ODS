
from django.db import models
from django.utils import timezone

# Creacion de campos de la tabla 'usuarios'

class Usuarios(models.Model):
    nombre = models.CharField(max_length=1000, default='DEFAULT_VALUE')
    img_perfil = models.FileField()
    web = models.CharField(max_length=700, default='DEFAULT_VALUE')
    descripcion = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'usuarios'