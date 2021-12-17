
from django.db import models
from django.utils import timezone

# Creacion de campos de la tabla 'detallesblog'

class DetallesBlog(models.Model):
    detalles = models.CharField(max_length=6000, default='DEFAULT_VALUE')
    logo = models.FileField()
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'detallesblog'
