# Generated by Django 5.0.6 on 2024-05-29 20:56

import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('full_name', models.CharField(max_length=50, verbose_name='nombres')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Mensajes',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=50, verbose_name='nombre')),
                ('descripcion', models.TextField()),
                ('about_title', models.CharField(max_length=50, verbose_name='titulo nosotros')),
                ('phone', models.CharField(max_length=10, verbose_name='telefono contacto')),
            ],
            options={
                'verbose_name': 'Pagina principal',
                'verbose_name_plural': 'Pagina principal',
            },
        ),
        migrations.CreateModel(
            name='Suscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Suscriptor',
                'verbose_name_plural': 'Suscripciones',
            },
        ),
    ]
