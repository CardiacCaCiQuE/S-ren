# Generated by Django 2.1.3 on 2018-11-09 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0004_auto_20181108_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='fotoMascota',
            field=models.ImageField(upload_to='Back/fotos'),
        ),
    ]