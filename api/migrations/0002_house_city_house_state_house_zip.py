# Generated by Django 4.1.7 on 2023-03-22 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='city',
            field=models.CharField(default=False, max_length=100000),
        ),
        migrations.AddField(
            model_name='house',
            name='state',
            field=models.CharField(default=False, max_length=100000),
        ),
        migrations.AddField(
            model_name='house',
            name='zip',
            field=models.CharField(default=False, max_length=100000),
        ),
    ]
