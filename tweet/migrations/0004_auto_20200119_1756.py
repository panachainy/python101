# Generated by Django 3.0.2 on 2020-01-19 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0003_auto_20200119_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='body',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='owner',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
