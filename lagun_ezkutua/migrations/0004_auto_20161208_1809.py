# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lagun_ezkutua', '0003_laguna_lagun_ezk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laguna',
            name='lagun_ezk',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
