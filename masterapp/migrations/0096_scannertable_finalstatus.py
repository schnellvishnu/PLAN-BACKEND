# Generated by Django 4.1.6 on 2024-04-08 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0095_company_companyflag_customers_customerflag_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scannertable',
            name='finalstatus',
            field=models.CharField(max_length=100, null=True),
        ),
    ]