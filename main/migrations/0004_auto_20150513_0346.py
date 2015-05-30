# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150512_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='condition',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(1)]),
        ),
    ]
