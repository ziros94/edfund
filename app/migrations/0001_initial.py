# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('club_name', models.CharField(max_length=200)),
                ('leader', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fund_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('club', models.ForeignKey(to='app.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Incentive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('description', models.CharField(max_length=200)),
                ('fund', models.ForeignKey(to='app.Fund')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='fund',
            field=models.ForeignKey(to='app.Fund'),
        ),
        migrations.AddField(
            model_name='club',
            name='school',
            field=models.ForeignKey(to='app.School'),
        ),
    ]
