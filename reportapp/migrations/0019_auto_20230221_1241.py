# Generated by Django 3.2.5 on 2023-02-21 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0018_auto_20230221_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productionreport',
            old_name='inProcess',
            new_name='inprocess',
        ),
        migrations.RenameField(
            model_name='productionreport',
            old_name='rejectedByCamera',
            new_name='rejectedbycamera',
        ),
    ]