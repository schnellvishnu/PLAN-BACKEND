# Generated by Django 4.1.6 on 2023-07-10 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0043_gtins'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Erpsetting',
        ),
        migrations.DeleteModel(
            name='Tracelinksettings',
        ),
        migrations.AddField(
            model_name='company',
            name='erp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='file_receiver',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='file_sender',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='sap_client',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='sap_destination',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='sap_language',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='sap_password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='sap_pool_size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='sap_server_host',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='sap_service',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='sap_system_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='sap_sytem_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='sap_user',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='sending_system',
            field=models.CharField(default='system1', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='sftp_host',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='sftp_password',
            field=models.CharField(default='password', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='sftp_port',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='sftp_username',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='siteid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='tracelink_password',
            field=models.CharField(default='password', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='tracelink_username',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
