# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import logger.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text_box', models.CharField(max_length=4000)),
                ('pub_date', models.DateTimeField(verbose_name=b'date created')),
                ('screen_shot', models.ImageField(max_length=1048576, null=True, upload_to=logger.models.get_image_path, blank=True)),
                ('original_document', models.FileField(max_length=1099511627776, null=True, upload_to=b'original_file', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
