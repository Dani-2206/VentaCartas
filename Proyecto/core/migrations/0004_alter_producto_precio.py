# Generated by Django 4.2.7 on 2023-11-07 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_producto_id_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(verbose_name='Precio del Producto'),
        ),
    ]
