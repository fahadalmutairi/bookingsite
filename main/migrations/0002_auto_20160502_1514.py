# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_end',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_start',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='owner',
            field=models.ForeignKey(related_name='owner', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='property_object',
            field=models.ForeignKey(blank=True, to='main.Property', null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='schedule',
            field=models.ForeignKey(blank=True, to='main.Schedule', null=True),
        ),
    ]
