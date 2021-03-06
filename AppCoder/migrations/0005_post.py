# Generated by Django 4.0.1 on 2022-02-26 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Titulo')),
                ('descripcion', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Descripcion')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
            ],
        ),
    ]
