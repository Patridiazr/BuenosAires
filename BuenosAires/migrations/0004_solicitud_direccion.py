# Generated by Django 2.2.2 on 2019-06-24 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BuenosAires', '0003_auto_20190623_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='direccion',
            field=models.CharField(default='default', max_length=100),
        ),
    ]
