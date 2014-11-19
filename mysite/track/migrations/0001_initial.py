# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(default=b'FR', max_length=2, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior')])),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'B', b'Boys'), (b'G', b'Girls')])),
                ('event_name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_dist', models.DecimalField(verbose_name=b'Time/Distance', max_digits=5, decimal_places=2)),
                ('date', models.DateField()),
                ('athlete', models.ForeignKey(default=1, to='track.Athlete')),
                ('event_name', models.ForeignKey(default=1, to='track.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='record',
            unique_together=set([('event_name', 'athlete')]),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('event_name', 'gender')]),
        ),
        migrations.AlterUniqueTogether(
            name='athlete',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]
