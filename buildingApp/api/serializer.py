from rest_framework import serializers
from buildingApp.models import Business, Building, Comment
from base.constants import GLOBAL_FIELDS_EXCLUDED
from rest_framework.validators import UniqueValidator


class SerializerBuilding(serializers.ModelSerializer):
    address = serializers.CharField(max_length=80,
                                    validators=[UniqueValidator(queryset=Building.objects.all())])
    business_name = serializers.CharField(source='business', read_only=True)

    class Meta:
        model = Building
        exclude = GLOBAL_FIELDS_EXCLUDED


class SerializerBusiness(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100,
                                 validators=[UniqueValidator(queryset=Business.objects.all())])
    buildingList = serializers.StringRelatedField(many=True)

    class Meta:
        model = Business
        exclude = GLOBAL_FIELDS_EXCLUDED


class SerializerComment(serializers.ModelSerializer):
    user = serializers.CharField(source='user_comment', read_only=True)

    class Meta:
        model = Comment
        exclude = GLOBAL_FIELDS_EXCLUDED + ['building', 'user_comment']
