# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0006_auto_20141124_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='image',
            field=models.ImageField(default=b'/media/profiles/sample.png', upload_to=b'/media/profiles/'),
            preserve_default=True,
        ),
    ]
