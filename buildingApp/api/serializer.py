from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from buildingApp.models import Business
from base.constants import GLOBAL_FIELDS_EXCLUDED
from django.db import models
from rest_framework.validators import UniqueValidator


class SerializerBusiness(serializers.ModelSerializer):
    class Meta:
        model = Business
        exclude = GLOBAL_FIELDS_EXCLUDED
