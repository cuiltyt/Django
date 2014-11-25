# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0008_auto_20141124_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='image',
        ),
    ]
