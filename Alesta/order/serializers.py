from rest_framework import serializers
from .models import Order, Service, Invoice


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['pk', 'name', 'quantity', 'price', 'currency',
                  'created_date', 'user', 'order', ]
        read_only_fields = ['pk', 'created_date', 'user', ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['pk', 'agent_name', 'auto_number',
                  'created_date', 'transporter', 'driver', 'user', ]
        read_only_fields = ['pk', 'created_date', 'user', ]


class InvoiceRetrieveSerializer(serializers.ModelSerializer):
    order = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()

    def get_order(self, obj) -> dict:
        order = Order.objects.get(pk=obj.order.pk)
        serializer = OrderSerializer(order)
        return serializer.data

    def get_services(self, obj) -> dict:
        queryset = Service.objects.filter(order=obj.order)
        serializer = ServiceSerializer(queryset, many=True)
        return serializer.data

    class Meta:
        model = Invoice
        fields = ['pk', 'invoice_number', 'created_date',
                  'requisites', 'order', 'services', ]


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['pk', 'invoice_number', 'created_date',
                  'requisites', 'order', ]
        read_only_fields = ['pk', 'created_date', ]
