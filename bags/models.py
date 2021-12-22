from django.db import models


class Bags(models.Model):
    COLOR_CHOICE = (
        (1, 'Black'),
        (2, 'White'),
        (3, 'Blue'),
        (4, 'Red'),
        (5, 'Pink'),
        (6, 'Green'),
        (7, 'Silver'),
    )
    image = models.ImageField(upload_to='bags/', blank=True, null=True)
    color = models.IntegerField(choices=COLOR_CHOICE)
    material = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
