from django.db import models
from shop.models import Product
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from phone_field import PhoneField


class Order(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    delivery = models.CharField(max_length=100, null=True, blank=True)
    verification = models.CharField(max_length=20)
    adress_choice = models.CharField(max_length=150, null=True)

    def __str__(self):
        return 'Заказ {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    class Meta:
        ordering = ('-create',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete = models.CASCADE)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    size = models.DecimalField(max_digits = 5, decimal_places = 1)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

class ShopAdress(models.Model):
    adress = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.adress

    class Meta:
        verbose_name = 'Адресс'
        verbose_name_plural = 'Адресса'
