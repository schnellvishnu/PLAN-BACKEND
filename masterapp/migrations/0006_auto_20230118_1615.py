# Generated by Django 3.2.5 on 2023-01-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0005_shippo_process_no_original'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hrf1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='hrf2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='hrf3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='hrf4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='hrf5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='hrf6',
            field=models.CharField(max_length=100, null=True),
        ),
    ]