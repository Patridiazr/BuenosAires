# Generated by Django 2.2.2 on 2019-06-24 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BuenosAires', '0002_auto_20190621_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProduI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('asunto', models.CharField(max_length=50)),
                ('mensaje', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre',
            new_name='username',
        ),
    ]
