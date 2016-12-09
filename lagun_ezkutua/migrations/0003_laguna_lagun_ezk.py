# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lagun_ezkutua', '0002_auto_20161205_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='laguna',
            name='lagun_ezk',
            field=models.ForeignKey(to='lagun_ezkutua.Laguna', null=True),
        ),
    ]
