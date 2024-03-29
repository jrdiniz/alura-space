# Generated by Django 4.2.6 on 2023-11-01 01:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0008_alter_photo_created_at_alter_photo_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_fk', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photo',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 1, 1, 26, 36, 588290, tzinfo=datetime.timezone.utc)),
        ),
    ]
