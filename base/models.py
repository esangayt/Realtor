from django.db import models
from simple_history.models import HistoricalRecords


class AppQuerySet(models.QuerySet):
    def delete(self):
        self.update(is_active=False)


class AppManager(models.Manager):
    def get_queryset(self):
        return AppQuerySet(self.model, using=self._db).exclude(is_active=False)

class BaseModel(models.Model):
    is_active = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField('Creation Date', auto_now_add=True)
    updated_at = models.DateTimeField('Modification Date', auto_now=True)
    deleted_at = models.DateTimeField('Removal date', null=True, blank=True)
    history = HistoricalRecords(inherit=True)
    objects = AppManager()

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos base'

    def delete(self):
        self.is_active = False
        self.save()

