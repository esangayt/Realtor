from rest_framework import generics, viewsets


class GeneralReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter()


class GeneralRPDViewSet(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter()


class GeneralCreateViewSet(generics.CreateAPIView):
    def get_queryset(self):
        model = self.get_serializer()
        return model.objects.all()


class GeneralListAPIView(generics.ListAPIView):

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        model = self.get_serializer().Meta.model
        return model.objects.filter(building=pk)


class GeneralModelViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter().order_by('id')
