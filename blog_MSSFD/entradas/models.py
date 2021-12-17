
from django.db import models
from django.utils import timezone

# Creacion de campos de la tabla 'entradas'

class Entradas(models.Model):
    titulo = models.CharField(max_length=5000, default='DEFAULT_VALUE')
    contenido = models.TextField(default='DEFAULT_VALUE')
    img_destacada = models.FileField()
    slug = models.CharField(max_length=5000, default='DEFAULT_VALUE') ## para url amigable
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'entradas'
