# Generated by Django 4.1.6 on 2024-02-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_loginmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginmodel',
            name='loginuname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
