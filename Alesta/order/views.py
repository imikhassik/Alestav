from django.db.models import Sum
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Order, Service, Invoice
from .serializers import OrderSerializer, ServiceSerializer, \
    InvoiceRetrieveSerializer, InvoiceSerializer


@extend_schema(tags=['Заказы'])
class OrderViewset(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=['Услуги'])
class ServiceViewset(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, url_path='total_service_sum/(?P<from_date>[^/.]+)/(?P<to_date>[^/.]+)')
    def total_service_sum(self, request, from_date, to_date):
        queryset = Service.objects.filter(created_date__range=(from_date, to_date))
        total_sum = queryset.aggregate(Sum('price'))
        return Response(total_sum)


@extend_schema(tags=['Счета'])
class InvoiceRetrieveViewset(mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceRetrieveSerializer


@extend_schema(tags=['Счета'])
class InvoiceViewset(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
