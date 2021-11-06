# Generated by Django 3.2.8 on 2021-11-03 21:11

import chat.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message_header_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='header_image',
        ),
        migrations.AddField(
            model_name='message',
            name='profile_image',
            field=models.ImageField(blank=True, default=chat.models.get_default_profile_image, max_length=255, null=True, upload_to=chat.models.get_profile_image_filepath),
        ),
    ]