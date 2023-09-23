from rest_framework.exceptions import ValidationError

from base.models import BaseModel
from django.db import models


class Business(BaseModel):
    name = models.CharField(max_length=100)
    page = models.URLField(max_length=150)

    class Meta:
        verbose_name = 'Name of Business'
        verbose_name_plural = 'Names of Business'
    def __str__(self):
        return self.name
