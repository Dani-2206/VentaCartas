# Generated by Django 4.2.5 on 2023-10-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_producto_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='cartas',
            field=models.CharField(max_length=20, null=True, verbose_name='ID del producto'),
        ),
    ]