# Generated by Django 3.2.5 on 2023-12-08 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0063_printerdatatable_responsefield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printerdatatable',
            name='responsefield',
            field=models.BooleanField(null=True),
        ),
    ]
