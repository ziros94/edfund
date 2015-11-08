# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151108_0123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club',
            options={'ordering': ['club_name']},
        ),
        migrations.AlterModelOptions(
            name='fund',
            options={'ordering': ['fund_name']},
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ['school_name']},
        ),
    ]
