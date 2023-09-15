# Generated by Django 4.2.4 on 2023-08-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Nombre de usuario')),
                ('email', models.CharField(max_length=100, verbose_name='Correo Electronico')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=100, verbose_name='apellido')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
                ('region', models.CharField(max_length=100, verbose_name='Region')),
                ('telefono', models.IntegerField(verbose_name='numero de telefono')),
                ('foto', models.ImageField(upload_to='perfil/', verbose_name='Imagen de perfil')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_administrado', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
