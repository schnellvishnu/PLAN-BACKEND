# Generated by Django 4.1.6 on 2023-04-03 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0023_alter_product_hrf1_alter_product_hrf2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Serial_Num_Provider_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='finished_good_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='location_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='regulation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sscc_prn',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
