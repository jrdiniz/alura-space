# Generated by Django 4.2.6 on 2023-10-29 00:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_alter_photo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 29, 0, 8, 59, 205574, tzinfo=datetime.timezone.utc)),
        ),
    ]