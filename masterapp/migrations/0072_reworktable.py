# Generated by Django 4.1.6 on 2023-12-16 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0071_scannertable_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReworkTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gtin', models.CharField(max_length=100, null=True)),
                ('slnonumber', models.CharField(max_length=100, null=True)),
                ('oldstatus', models.CharField(max_length=100, null=True)),
                ('newstatus', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
