# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('categoria_id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to=b'')),
                ('nro_serie', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('costo', models.IntegerField()),
                ('precio_unitario', models.IntegerField()),
                ('categoria', models.ForeignKey(to='producto.Categoria')),
                ('marca', models.ForeignKey(to='producto.Marca')),
            ],
        ),
    ]
