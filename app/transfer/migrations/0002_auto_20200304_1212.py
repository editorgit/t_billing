# Generated by Django 3.0.4 on 2020-03-04 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MoneyConversions',
            new_name='MoneyConversion',
        ),
    ]
