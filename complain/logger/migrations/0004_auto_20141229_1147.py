# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import logger.models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0003_auto_20141223_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='original_document',
            field=models.FileField(max_length=1099511627776, null=True, upload_to=logger.models.get_image_path, blank=True),
            preserve_default=True,
        ),
    ]
