# Generated by Django 4.1.6 on 2024-02-27 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0090_printerdatatable_loadpause'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printerdatatable',
            name='start_pause_btnresponse',
            field=models.BooleanField(default=False),
        ),
    ]