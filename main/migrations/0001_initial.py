# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('first_name', models.CharField(max_length=255, null=True, verbose_name=b'first name', blank=True)),
                ('last_name', models.CharField(max_length=255, null=True, verbose_name=b'last name', blank=True)),
                ('is_owner', models.BooleanField(default=False, verbose_name=b'owner status')),
                ('is_staff', models.BooleanField(default=False, verbose_name=b'staff status')),
                ('is_active', models.BooleanField(default=False, verbose_name=b'active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name=b'date joined')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=255)),
                ('governorate', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('icon', models.ImageField(null=True, upload_to=b'amenities_icons', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_start', models.DateField(null=True, blank=True)),
                ('date_end', models.DateField(null=True, blank=True)),
                ('booked', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(related_name='owner', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('bedrooms', models.IntegerField(null=True, blank=True)),
                ('floors', models.IntegerField()),
                ('rate_by_day', models.IntegerField(null=True, blank=True)),
                ('rate_by_week', models.IntegerField(null=True, blank=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('property_type_choices', models.CharField(default=b'Farm', max_length=255, choices=[(b'Apartment', b'Apartment'), (b'Chalet', b'Chalet'), (b'Farm', b'Farm')])),
                ('address', models.ForeignKey(blank=True, to='main.Address', null=True)),
                ('amenities', models.ManyToManyField(to='main.Amenities')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'property_images')),
                ('property_object', models.ForeignKey(to='main.Property')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating_by_user', models.IntegerField()),
                ('property_object', models.ForeignKey(to='main.Property')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('property_object', models.ForeignKey(to='main.Property')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule_2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Rdate', models.DateField()),
                ('Unavaliable', models.BooleanField(default=False)),
                ('booked', models.BooleanField(default=False)),
                ('property_o', models.ForeignKey(to='main.Property')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='property_object',
            field=models.ForeignKey(blank=True, to='main.Property', null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='schedule',
            field=models.ForeignKey(blank=True, to='main.Schedule', null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(related_name='user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
