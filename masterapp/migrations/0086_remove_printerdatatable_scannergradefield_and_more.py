# Generated by Django 4.1.6 on 2024-02-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0085_printerdatatable_scannergradefield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='printerdatatable',
            name='scannergradefield',
        ),
        migrations.AlterField(
            model_name='printerdatatable',
            name='return_slno_btn_response',
            field=models.BooleanField(default=False),
        ),
    ]
