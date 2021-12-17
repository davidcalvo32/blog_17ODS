from django.db import models
from django.utils import timezone

# Creacion de campos de la tabla 'categorias'

class Categorias(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT_VALUE')
    detalles = models.CharField(max_length=1000, default='DEFAULT_VALUE')
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'categorias'


