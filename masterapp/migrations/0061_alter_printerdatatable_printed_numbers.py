# Generated by Django 4.1.6 on 2023-11-25 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0060_printerdatatable_printed_numbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printerdatatable',
            name='printed_numbers',
            field=models.JSONField(null=True),
        ),
    ]
