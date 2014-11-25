# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0003_athlete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='image',
            field=models.ImageField(default=b'/static/images/sample.png', upload_to=b'~/dev/django/mysite/track/static/images/'),
            preserve_default=True,
        ),
    ]
