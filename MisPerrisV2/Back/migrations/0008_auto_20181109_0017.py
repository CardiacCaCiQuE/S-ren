# Generated by Django 2.1.3 on 2018-11-09 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0007_auto_20181109_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='fotoMascota',
            field=models.ImageField(default='Sistema/static/media/perros/noname.jpg', upload_to='', verbose_name='Back/static/media/perros'),
        ),
    ]
