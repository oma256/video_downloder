# Generated by Django 2.1.3 on 2019-05-08 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_converter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='queryhistory',
            old_name='link',
            new_name='url',
        ),
    ]
