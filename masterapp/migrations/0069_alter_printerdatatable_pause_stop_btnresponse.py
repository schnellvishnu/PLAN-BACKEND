# Generated by Django 4.1.6 on 2023-12-12 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0068_printerdatatable_pause_stop_btnresponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printerdatatable',
            name='pause_stop_btnresponse',
            field=models.BooleanField(default=False),
        ),
    ]