from django.db import models


class Order(models.Model):

        name = models.CharField("Наименование агента", max_length=255)
        number = models.CharField("Номер авто", max_length=20)
        date = models.DateTimeField("Дата заказа",auto_now_add=True)
        name1 = models.CharField("Перевозчик", max_length=255)
        name2 = models.CharField("Водитель", max_length=255)
        name3 = models.CharField("Пользователь", max_length=255)


class Meta:
    ordering = ('-created',)
    verbose_name = "Заказ"
    verbose_name_plural = "Заказы"


    def __str__(self):
        return "Заказ #{0}".format(str(self.id))
