from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework.exceptions import ValidationError

from base.models import BaseModel
from django.db import models


def unique_value(value):
    business = Business.objects.filter(name=value)

    if business.exists():
        raise ValidationError("Name invalid")

    return value


class Business(BaseModel):
    name = models.CharField(max_length=100)
    page = models.URLField(max_length=150)

    class Meta:
        verbose_name = 'Name of Business'
        verbose_name_plural = 'Names of Business'

    def __str__(self):
        return self.name


class Building(BaseModel):
    address = models.CharField(max_length=80)
    country = models.CharField(max_length=70)
    description = models.CharField(max_length=250)
    imageUri = models.URLField(max_length=250)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='buildingList')

    class Meta:
        verbose_name = 'Building'
        verbose_name_plural = 'Buildings'

    def __str__(self):
        return f'Building: {self.address}'


class Comment(BaseModel):
    qualifying = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="buildingList")
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f'{self.description}'
