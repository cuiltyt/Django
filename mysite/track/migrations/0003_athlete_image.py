# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_auto_20141029_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='image',
            field=models.ImageField(default=b'/static/images/sample.png', upload_to=b''),
            preserve_default=True,
        ),
    ]
