from django.db import models


class Product(models.Model):
    name = models.CharField('商品名', max_length=100)
    description = models.TextField('説明', null=True)
    price = models.PositiveIntegerField('価格')
    quantity = models.PositiveIntegerField('在庫')
    published_on = models.DateField('発売日')

    @property
    def is_in_stock(self):
        return self.quantity > 0
