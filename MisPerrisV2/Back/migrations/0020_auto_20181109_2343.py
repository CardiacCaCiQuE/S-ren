# Generated by Django 2.1.3 on 2018-11-10 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0019_auto_20181109_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='fotoMascota',
            field=models.FileField(upload_to=''),
        ),
    ]
