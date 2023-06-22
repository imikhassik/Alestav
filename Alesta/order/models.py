from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):

    agent_name = models.CharField("Наименование агента", max_length=255)
    auto_number = models.CharField("Номер авто", max_length=20)
    created_date = models.DateTimeField("Дата заказа", auto_now_add=True)
    transporter = models.CharField("Перевозчик", max_length=255)
    driver = models.CharField("Водитель", max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_date',)
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return "Заказ #{0}".format(str(self.pk))


class Service(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()
    currency = models.CharField(max_length=3)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='services', on_delete=models.CASCADE)


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    requisites = models.JSONField()
    order = models.OneToOneField(Order, related_name='invoice', on_delete=models.CASCADE)
