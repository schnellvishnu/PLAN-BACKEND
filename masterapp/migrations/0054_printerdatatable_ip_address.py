# Generated by Django 4.1.6 on 2023-10-31 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0053_printerdatatable_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='printerdatatable',
            name='ip_address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
