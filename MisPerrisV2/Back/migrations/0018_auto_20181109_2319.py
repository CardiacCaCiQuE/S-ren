# Generated by Django 2.1.3 on 2018-11-10 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0017_auto_20181109_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='fotoMascota',
            field=models.ImageField(default='media', upload_to='media'),
        ),
    ]
