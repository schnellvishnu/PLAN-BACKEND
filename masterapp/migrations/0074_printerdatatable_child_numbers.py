# Generated by Django 4.1.6 on 2024-01-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0073_printerdatatable_label_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='printerdatatable',
            name='child_numbers',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
