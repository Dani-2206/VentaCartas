
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_rename_usuario_administrado_usuario_usuario_administrador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(upload_to='perfil/', verbose_name='Imagen de perfil'),
        ),
    ]
