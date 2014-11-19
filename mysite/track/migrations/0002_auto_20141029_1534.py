# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='gender',
            field=models.CharField(max_length=1, choices=[(b'B', b'Boy'), (b'G', b'Girl')]),
            preserve_default=True,
        ),
    ]
