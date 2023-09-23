from rest_framework import generics, viewsets


class GeneralListAPIView(generics.ListAPIView):

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(is_active=True)


class GeneralAPIView(generics.GenericAPIView):

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(is_active=True)


class GeneralModelViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(is_active=True).order_by('id')
