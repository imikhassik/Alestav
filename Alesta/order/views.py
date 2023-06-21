from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework import mixins

from .models import Order, Service, Invoice
from .serializers import OrderSerializer, ServiceSerializer, InvoiceSerializer


@extend_schema(tags=['orders'])
class OrderViewset(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@extend_schema(tags=['services'])
class ServiceViewset(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


@extend_schema(tags=['invoices'])
class InvoiceViewset(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
