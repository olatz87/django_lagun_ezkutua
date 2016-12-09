# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lagun_ezkutua', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kuadrilla',
            name='kuadri_izena',
        ),
        migrations.AddField(
            model_name='kuadrilla',
            name='lagun_kopurua',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
