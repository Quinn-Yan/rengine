# Generated by Django 3.0.7 on 2020-07-28 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0003_auto_20200728_1905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scanactivity',
            old_name='scan_of',
            new_name='scan_id',
        ),
    ]
