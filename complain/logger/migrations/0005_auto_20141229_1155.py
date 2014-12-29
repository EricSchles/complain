# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0004_auto_20141229_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='original_document',
            field=models.FileField(max_length=1099511627776, null=True, upload_to=b'/media/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='complaint',
            name='screen_shot',
            field=models.ImageField(max_length=1048576, null=True, upload_to=b'/media/', blank=True),
            preserve_default=True,
        ),
    ]
