# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0017_auto_20150429_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageview',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
