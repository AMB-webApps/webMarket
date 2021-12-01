from django.db import models

BRAND_CHOICES = [
    (1, 'HP'),
    (2, 'DELL'),
    (3, 'LENOVO'),
    (4, ',SI'),
    (5, 'ACER'),
    (6, 'SAMSUNG'),
    (7, 'ASUS'),
    (8, 'APPLE'),
    (9, 'TOSHIBA'),
    (10, 'SONY'),
    (11, 'RAZER'),
    (12, 'LG'),
]

USES_CHOICES = [
    (1, 'New'),
    (2, 'Used'),
]


class Product(models.Model):
    brand = models.PositiveSmallIntegerField(choices=BRAND_CHOICES)
    name = models.CharField(max_length=300)
    display = models.CharField(max_length=200)
    cpu = models.CharField(max_length=200)
    memory = models.CharField(max_length=200)
    ssd_hdd = models.CharField(max_length=200)
    graphic_card = models.CharField(max_length=200)
    uses = models.PositiveSmallIntegerField(choices=USES_CHOICES)
    model = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    image = models.ImageField(many=True)

    def __str__(self):
        return f'{self.brand}, {self.name}, {self.display}, {self.cpu}, {self.memory}, {self.ssd_hdd}, ' \
               f'{self.graphic_card}, {self.uses}, {self.model}, {self.price}, {self.image}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'product'
