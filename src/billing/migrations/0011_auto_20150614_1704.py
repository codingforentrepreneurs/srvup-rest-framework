# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0010_auto_20150429_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_end',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'End Date'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_start',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Start Date'),
        ),
    ]
