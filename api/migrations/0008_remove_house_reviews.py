# Generated by Django 4.1.7 on 2023-04-04 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_sqft_house_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='reviews',
        ),
    ]
