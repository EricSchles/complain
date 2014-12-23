# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0002_auto_20141223_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=b'date created', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='complaint',
            name='text_box',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
