# Generated by Django 4.0 on 2022-01-16 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_alter_user_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='city_id',
        ),
    ]
