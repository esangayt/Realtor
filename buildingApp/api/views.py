import datetime

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from base.CustomResponse import CustomResponse
from base.api import GeneralModelViewSet
from buildingApp.api.serializer import SerializerBusiness
from buildingApp.models import Business
from rest_framework.pagination import PageNumberPagination


class BusinessViewSet(GeneralModelViewSet):
    serializer_class = SerializerBusiness

    def list(self, request, *args, **kwargs):
        business_serializer = self.get_serializer(self.get_queryset(), many=True)
        print(type(self.paginate_queryset(self.get_queryset())))
        return Response(business_serializer.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            business = Business.objects.get(id=kwargs.get('pk'), is_active=True)
            business_serializer = self.get_serializer(business)

            return CustomResponse.item(business_serializer.data)
        except Business.DoesNotExist:
            return CustomResponse.item()

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
            business = Business.objects.get(id=kwargs.get('pk'), is_active=True)
            business.is_active = False
            # business.deleted_at = datetime.datetime.now()
            business.save()
            return CustomResponse.destroyed(content="Deleted", message="Deleted")
        except Business.DoesNotExist:
            return CustomResponse.item()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return CustomResponse.stored(serializer.data)
        return CustomResponse(serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)
