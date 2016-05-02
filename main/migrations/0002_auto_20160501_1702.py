# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '__first__'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='property_object',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='property',
            name='booking_item',
            field=models.ForeignKey(default=datetime.datetime(2016, 5, 1, 17, 2, 16, 821742, tzinfo=utc), to='booking.BookingItem'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
