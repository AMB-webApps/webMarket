# Generated by Django 3.2.9 on 2021-12-02 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0002_auto_20211202_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/%Y/%m/%d'),
        ),
    ]
