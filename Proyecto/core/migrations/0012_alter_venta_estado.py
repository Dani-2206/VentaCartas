# Generated by Django 4.0.3 on 2023-11-23 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_venta_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='estado',
            field=models.CharField(default='En Tienda', max_length=20),
        ),
    ]
