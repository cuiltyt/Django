# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0005_auto_20141124_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='image',
            field=models.ImageField(default=b'/media/sample.png', upload_to=b'profiles/'),
            preserve_default=True,
        ),
    ]
