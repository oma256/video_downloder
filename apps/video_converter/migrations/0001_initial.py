# Generated by Django 2.1.3 on 2019-05-05 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QueryHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=500, verbose_name='video link')),
                ('query_date', models.DateTimeField(auto_now_add=True, verbose_name='query date')),
            ],
        ),
    ]