from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response

from .models import Order, Service, Invoice
from .serializers import OrderSerializer, ServiceSerializer, \
    InvoiceRetrieveSerializer, InvoiceSerializer


@extend_schema(tags=['orders'])
class OrderViewset(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=['services'])
class ServiceViewset(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=['invoices'])
class InvoiceRetrieveViewset(mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceRetrieveSerializer


@extend_schema(tags=['invoices'])
class InvoiceViewset(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
