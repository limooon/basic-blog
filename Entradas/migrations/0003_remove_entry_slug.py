# Generated by Django 5.0.6 on 2024-05-29 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Entradas', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='slug',
        ),
    ]
