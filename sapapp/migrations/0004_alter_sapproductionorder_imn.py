# Generated by Django 3.2.5 on 2023-02-02 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sapapp', '0003_alter_sapproductionorder_imn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sapproductionorder',
            name='imn',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]