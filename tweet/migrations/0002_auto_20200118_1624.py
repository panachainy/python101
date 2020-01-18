# Generated by Django 3.0.2 on 2020-01-18 16:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='tweet',
            name='is_retweet',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tweet',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
