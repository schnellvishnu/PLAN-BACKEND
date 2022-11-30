# Generated by Django 3.2.16 on 2022-11-18 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BarCodeType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Barcodetypename', models.CharField(max_length=20, unique=True)),
                ('labelxml', models.FileField(null=True, upload_to='')),
                ('constant_encoding_fields', models.JSONField(blank=True, null=True)),
                ('nonconstant_encoding_fields', models.JSONField(blank=True, null=True)),
                ('nonconstant_nonencoding_fields', models.JSONField(blank=True, null=True)),
                ('variable_fields', models.JSONField(blank=True, null=True)),
                ('display_only_fields', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('created_at', models.DateField(null=True)),
                ('updated_at', models.DateField(null=True)),
                ('created_by', models.CharField(max_length=100)),
                ('central_repository_api_secret', models.CharField(max_length=100)),
                ('gln', models.CharField(max_length=20)),
                ('gs1_company_prefix', models.CharField(max_length=20)),
                ('landmark', models.CharField(blank=True, max_length=20, null=True)),
                ('sgln_extension', models.CharField(max_length=100)),
                ('to_businessparty_lookupfield', models.CharField(max_length=20)),
                ('tracelink_file_receiver', models.CharField(max_length=100)),
                ('erp', models.CharField(max_length=100)),
                ('sap_client', models.CharField(max_length=100)),
                ('sap_service', models.CharField(max_length=100)),
                ('sap_destination', models.CharField(max_length=100)),
                ('sap_language', models.CharField(max_length=100)),
                ('sap_password', models.CharField(max_length=100)),
                ('sap_pool_size', models.CharField(max_length=100)),
                ('sap_server_host', models.CharField(max_length=100)),
                ('sap_system_id', models.CharField(max_length=100)),
                ('sap_sytem_number', models.CharField(max_length=100)),
                ('sap_user', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('created_by', models.CharField(max_length=100)),
                ('company_prefix', models.CharField(max_length=20)),
                ('company_gln', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('zip', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ShipToLocationLookupid', models.CharField(blank=True, max_length=100, null=True)),
                ('group', models.CharField(blank=True, choices=[('CMO', 'CMO'), ('CPO', 'CPO'), ('Customer', 'Customer'), ('Destroyer', 'Destroyer'), ('Hospital', 'Hospital'), ('Manufacture', 'Manufacture'), ('Pharmacy', 'Pharmacy'), ('Transporter', 'Transporter'), ('Warehouse', 'Warehouse'), ('Wholesaler', 'Wholesaler')], max_length=40, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_by', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=40)),
                ('loc_gln', models.CharField(max_length=20, unique=True)),
                ('ShipToLocationLookupid', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('address', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('zip', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers_to_locations', to='masterapp.customers')),
            ],
        ),
        migrations.CreateModel(
            name='SnProvider',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=100)),
                ('requested_link', models.CharField(blank=True, max_length=100, null=True)),
                ('requested_xml', models.TextField(blank=True, null=True)),
                ('commisioning_link', models.CharField(blank=True, max_length=100, null=True)),
                ('commisioning_xml', models.TextField(blank=True, null=True)),
                ('aggregation_link', models.CharField(blank=True, max_length=100, null=True)),
                ('aggregation_xml', models.TextField(blank=True, null=True)),
                ('destroy_link', models.CharField(blank=True, max_length=100, null=True)),
                ('destroy_xml', models.TextField(blank=True, null=True)),
                ('shipping_link', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping_xml', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productionorder_num', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('batch_num', models.CharField(max_length=50)),
                ('requested', models.CharField(max_length=50)),
                ('stock_quantity', models.CharField(max_length=50)),
                ('shipped', models.CharField(max_length=50)),
                ('removed', models.CharField(max_length=50)),
                ('standard', models.CharField(max_length=250)),
                ('expiration_date', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ShipPO',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shipping_order_name', models.CharField(max_length=40)),
                ('shipping_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=100)),
                ('shipping_type', models.CharField(default='item', max_length=20)),
                ('batch_for_export', models.CharField(blank=True, max_length=100, null=True)),
                ('exempted_from_barcoding', models.CharField(blank=True, max_length=100, null=True)),
                ('exemption_notification_and_date', models.CharField(blank=True, max_length=100, null=True)),
                ('exempted_country_code', models.CharField(blank=True, max_length=100, null=True)),
                ('sold_to', models.CharField(blank=True, max_length=100, null=True)),
                ('delivery_number', models.CharField(blank=True, max_length=100, null=True)),
                ('delivary_number', models.CharField(blank=True, max_length=100, null=True)),
                ('advance_ship_notice', models.CharField(blank=True, max_length=100, null=True)),
                ('destination_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations_to_shipping', to='masterapp.locations')),
                ('source_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_to_shippo', to='masterapp.locations')),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers_to_shippingpo', to='masterapp.customers')),
            ],
        ),
    ]