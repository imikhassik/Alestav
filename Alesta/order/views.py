from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.schemas.openapi import AutoSchema

from .models import Order, Service, Invoice
from .serializers import OrderSerializer, ServiceSerializer, InvoiceSerializer


class OrderViewset(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    schema = AutoSchema(tags=["Orders"])


class ServiceViewset(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    schema = AutoSchema(tags=["Services"])


class InvoiceViewset(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    schema = AutoSchema(tags=["Invoices"])
