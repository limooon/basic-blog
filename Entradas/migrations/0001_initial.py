# Generated by Django 5.0.6 on 2024-05-29 20:56

import ckeditor_uploader.fields
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('short_name', models.CharField(max_length=50, unique=True, verbose_name='nombre corto')),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Etiqueta',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=50, verbose_name='titulo')),
                ('resume', models.TextField(verbose_name='resumen')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='contenido')),
                ('public', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='Entry', verbose_name='imagen')),
                ('portada', models.BooleanField(default=False)),
                ('in_home', models.BooleanField(default=False)),
                ('slug', models.SlugField(editable=False, max_length=300)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entradas.category')),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
            },
        ),
    ]
