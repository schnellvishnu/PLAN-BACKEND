# Generated by Django 4.1.6 on 2023-04-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0024_alter_product_serial_num_provider_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='hrf1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='hrf2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='hrf3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='hrf4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='hrf5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='hrf6',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
