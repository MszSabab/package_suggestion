# Generated by Django 4.0.3 on 2022-03-26 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package_app', '0005_alter_package_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.IntegerField(blank=True),
        ),
    ]