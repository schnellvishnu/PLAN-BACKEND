# Generated by Django 4.1.6 on 2023-08-07 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0050_company_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='landmark',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='sgln_extension',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='tobusinessparylookupid',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
