# Generated by Django 4.1.6 on 2023-04-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0034_alter_shippo_shipping_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippo',
            name='shipping_date',
            field=models.DateField(null=True),
        ),
    ]