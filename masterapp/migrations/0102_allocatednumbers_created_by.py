# Generated by Django 4.1.6 on 2024-05-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0101_allocatednumbers'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocatednumbers',
            name='created_by',
            field=models.CharField(default=False, max_length=100),
        ),
    ]