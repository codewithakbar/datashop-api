from django.db import models
from cart.models import Cart

from products.models import Product

from django.contrib.auth import get_user_model


User = get_user_model()


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )

    DOSTAVKA = (
        ("Bo\'rib olish", "Bo\'rib olish"),
        ("Dastavka", "Dastavka")
    )

    PAYMENT_METHOD = (
        ('Click', 'Click'),
        ('Payme', 'Payme'),
        ('Naqd', 'Naqd'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Cart, on_delete=models.CASCADE)

    # 1. Как вы хотите получить заказ?
    dostavka = models.CharField(max_length=34, choices=DOSTAVKA, default="Dastavka")

    # 2. Укажите адрес доставки
    country = models.CharField(blank=True, max_length=20)
    city = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)

    # 3. Выберите способ оплаты
    pay_metod = models.CharField(max_length=23, choices=PAYMENT_METHOD, default='Naqd')

    # 4. Контактное имя
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone = models.CharField(blank=True, max_length=20)


    def __str__(self):
        return self.user.first_name
    
