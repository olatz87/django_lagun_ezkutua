# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kuadrilla',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('kuadri_izena', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Laguna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('izena', models.CharField(max_length=200)),
                ('eposta', models.EmailField(max_length=254)),
                ('kuadri', models.ForeignKey(to='lagun_ezkutua.Kuadrilla')),
            ],
        ),
    ]
