# Generated by Django 2.1.3 on 2018-11-08 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('codigoMascota', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='./Back/static/fotos/')),
                ('nombreMascota', models.CharField(max_length=20)),
                ('razaMascota', models.CharField(max_length=50)),
                ('descripcionMascotra', models.TextField()),
                ('estadoMascota', models.CharField(default='Rescatado', max_length=50)),
            ],
        ),
    ]