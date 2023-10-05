from django.db import models
from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=128,unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=9,decimal_places=2)
    quintity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.name}'


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity