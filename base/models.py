from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.
class BaseModel(models.Model):
    is_active = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField('Creation Date', auto_now_add=True)
    updated_at = models.DateTimeField('Modification Date', auto_now=True)
    deleted_at = models.DateTimeField('Removal date', null=True, blank=True)
    history = HistoricalRecords()

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos base'
