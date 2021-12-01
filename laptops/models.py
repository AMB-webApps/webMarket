from django.db import models


class Product(models.Model):

    class BrandChoice(models.TextChoices):
        hp = 'HP'
        dell = 'DELL'
        lenovo = 'LENOVO'
        msi = 'MSI'
        acer = 'ACER'
        samsung = 'SAMSUNG'
        asus = 'ASUS'
        apple = 'APPLE'
        toshiba = 'TOSHIBA'
        sony = 'SONY'
        razer = 'RAZER'
        lg = 'LG'

    class UsesChoice(models.TextChoices):
        new = "Новый"
        bu = "Бучный"

    brand = models.CharField(max_length=200, choices=BrandChoice)
    name = models.CharField(max_length=300)
    display = models.CharField(max_length=200)
    cpu = models.CharField(max_length=200)
    memory = models.CharField(max_length=200)
    ssd_hdd = models.CharField(max_length=200)
    graphic_card = models.CharField(max_length=200)
    uses = models.CharField(max_length=20, choices=UsesChoice)
    model = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    image = models.ImageField(many=True)

