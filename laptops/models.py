from django.db import models


class Product(models.Model):

    HP = 'Hp'
    DELL = 'DELL'
    LENOVO = 'LENOVO'
    SI = 'SI'
    ACER = 'ACER'
    SAMSUNG = 'SAMSUNG'
    ASUS = 'ASUS'
    APPLE = 'APPLE'
    TOSHIBA = 'TOSHIBA'
    SONY = 'SONY'
    RAZER = 'RAZER'
    LG = 'LG'

    BRAND_CHOICES = (
        (HP, 'HP'),
        (DELL, 'DELL'),
        (LENOVO, 'LENOVO'),
        (SI, 'SI'),
        (ACER, 'ACER'),
        (SAMSUNG, 'SAMSUNG'),
        (ASUS, 'ASUS'),
        (APPLE, 'APPLE'),
        (TOSHIBA, 'TOSHIBA'),
        (SONY, 'SONY'),
        (RAZER, 'RAZER'),
        (LG, 'LG'),
    )

    NEW = 'New'
    USED = 'Used'

    USES_CHOICES = (
        (NEW, 'New'),
        (USED, 'Used'),
)

    brand = models.CharField(max_length=10, choices=BRAND_CHOICES, default=APPLE)
    name = models.CharField(max_length=300)
    display = models.CharField(max_length=200)
    cpu = models.CharField(max_length=200)
    memory = models.CharField(max_length=200)
    ssd_hdd = models.CharField(max_length=200)
    graphic_card = models.CharField(max_length=200)
    uses = models.CharField(max_length=4, choices=USES_CHOICES, default=NEW)
    model = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'{self.brand}, {self.name}, {self.uses}, {self.price}, {self.image}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'products'
