# Generated by Django 2.2.2 on 2019-06-23 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BuenosAires', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitud',
            old_name='mensaje',
            new_name='men',
        ),
    ]