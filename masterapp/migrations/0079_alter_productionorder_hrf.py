# Generated by Django 4.1.6 on 2024-02-05 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0078_alter_productionorder_hrf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionorder',
            name='hrf',
            field=models.JSONField(default='{"hrf1":null,"hrf2":null,"hrf3":null,"hrf4":null,"hrf5":null,"hrf6":null,"hrf1Value":"","hrf2Value":"","hrf3Value":"","hrf4Value":"","hrf5Value":"","hrf6Value":""}', max_length=200),
        ),
    ]
