# Generated by Django 4.0.3 on 2022-03-26 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package_app', '0002_package_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='details',
        ),
        migrations.RemoveField(
            model_name='service',
            name='price',
        ),
        migrations.RemoveField(
            model_name='service',
            name='status',
        ),
        migrations.RemoveField(
            model_name='service',
            name='view_order',
        ),
    ]
