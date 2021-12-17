from django.db import models
from django.db.models.fields import DateTimeField

from django.utils import timezone

# creacion de campos de la tabla detallesblog

class DetallesBlog(models.Model):
    detalles = models.CharField(max_length=6000, default='DEFAULT_VALUE')
    logo = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'detallesblog'
