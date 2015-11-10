# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151108_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='description',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
