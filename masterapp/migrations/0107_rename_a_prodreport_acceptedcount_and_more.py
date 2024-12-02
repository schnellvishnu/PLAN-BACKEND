# Generated by Django 4.1.6 on 2024-05-13 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0106_prodreport_production_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prodreport',
            old_name='A',
            new_name='acceptedcount',
        ),
        migrations.RenameField(
            model_name='prodreport',
            old_name='B',
            new_name='challengedcount',
        ),
        migrations.RenameField(
            model_name='prodreport',
            old_name='C',
            new_name='damagedcount',
        ),
        migrations.RenameField(
            model_name='prodreport',
            old_name='D',
            new_name='inprocesscount',
        ),
        migrations.RenameField(
            model_name='prodreport',
            old_name='E',
            new_name='rejectedbycameracount',
        ),
        migrations.RenameField(
            model_name='prodreport',
            old_name='F',
            new_name='samplecount',
        ),
        migrations.RenameField(
            model_name='prodreport',
            old_name='G',
            new_name='specimencount',
        ),
        migrations.RenameField(
            model_name='prodreport',
            old_name='H',
            new_name='teachcount',
        ),
        migrations.RenameField(
            model_name='prodreport',
            old_name='I',
            new_name='unusedcount',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='J',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='K',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='L',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='M',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='N',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='O',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='P',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='Q',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='R',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='S',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='T',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='U',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='V',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='W',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='X',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='Y',
        ),
        migrations.RemoveField(
            model_name='prodreport',
            name='Z',
        ),
    ]
