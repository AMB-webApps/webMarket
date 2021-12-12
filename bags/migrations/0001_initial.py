# Generated by Django 3.2.9 on 2021-12-12 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='bags/%Y/%m/%d')),
                ('color', models.CharField(choices=[(1, 'Black'), (2, 'White'), (3, 'Blue'), (4, 'Red'), (5, 'Pink'), (6, 'Green'), (7, 'Silver')], max_length=10)),
                ('material', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
    ]
