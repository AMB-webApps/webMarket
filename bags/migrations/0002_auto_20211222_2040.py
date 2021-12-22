# Generated by Django 3.2.9 on 2021-12-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bags',
            name='color',
            field=models.IntegerField(choices=[(1, 'Black'), (2, 'White'), (3, 'Blue'), (4, 'Red'), (5, 'Pink'), (6, 'Green'), (7, 'Silver')]),
        ),
        migrations.AlterField(
            model_name='bags',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='bags/'),
        ),
    ]
