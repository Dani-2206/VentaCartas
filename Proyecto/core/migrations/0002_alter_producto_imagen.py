# Generated by Django 4.2.4 on 2023-08-18 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='productos/', verbose_name='foto de la carta'),
        ),
    ]
