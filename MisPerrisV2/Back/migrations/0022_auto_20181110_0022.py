# Generated by Django 2.1.3 on 2018-11-10 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0021_auto_20181110_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='fotoMascota',
            field=models.ImageField(upload_to='Back/static/media/'),
        ),
    ]
