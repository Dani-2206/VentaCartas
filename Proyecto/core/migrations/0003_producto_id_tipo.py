# Generated by Django 4.2.5 on 2023-10-24 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tipo_alter_categoria_id_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='id_Tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.tipo'),
        ),
    ]
