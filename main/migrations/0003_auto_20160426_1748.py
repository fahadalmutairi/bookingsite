# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_property_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimages',
            name='image',
            field=models.ImageField(upload_to=b'property_images'),
        ),
    ]
