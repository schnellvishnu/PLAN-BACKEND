# Generated by Django 4.1.6 on 2024-02-05 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0080_alter_productionorder_hrf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionorder',
            name='hrf',
            field=models.JSONField(blank=True, default='{"hrf1":null,"hrf2":null,"hrf3":null,"hrf4":null,"hrf5":null,"hrf6":null,"hrf1Value":null,"hrf2Value":null,"hrf3Value":null,"hrf4Value":null,"hrf5Value":null,"hrf6Value":null}'),
        ),
    ]
