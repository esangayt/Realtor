import datetime

from django.contrib.auth.models import User
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from base.CustomResponse import CustomResponse
from base.api import (
    GeneralModelViewSet
)
from buildingApp.api.serializer import (
    SerializerBusiness, SerializerBuilding, SerializerComment
)
from buildingApp.models import Business, Building


class BusinessViewSet(GeneralModelViewSet):
    serializer_class = SerializerBusiness
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return CustomResponse.collection(serializer.data)

    def update(self, request, *args, **kwargs):
        try:
            business = Business.objects.get(id=kwargs.get('pk'), is_active=True)
            business_serializer = self.get_serializer(business, data=request.data, partial=True)

            if business_serializer.is_valid():
                business_serializer.save()
                return CustomResponse.updated(business_serializer.data)

            return CustomResponse(business_serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)
        except Business.DoesNotExist:
            return CustomResponse.item()

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)

            return CustomResponse.destroyed(content="Deleted", message="Delete")
        except Http404:
            return CustomResponse.item()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return CustomResponse.stored(serializer.data, headers=headers)
        return CustomResponse(serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)


class BuildingViewSet(GeneralModelViewSet):
    serializer_class = SerializerBuilding

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
