# Generated by Django 3.1 on 2020-08-08 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MtOrder',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('merchant_id', models.IntegerField()),
                ('client_id', models.IntegerField()),
                ('json_details', models.TextField(blank=True, null=True)),
                ('trans_type', models.CharField(max_length=100)),
                ('payment_type', models.CharField(max_length=100)),
                ('sub_total', models.FloatField()),
                ('tax', models.FloatField()),
                ('taxable_total', models.DecimalField(decimal_places=4, max_digits=14)),
                ('total_w_tax', models.FloatField()),
                ('status', models.CharField(max_length=255)),
                ('stats_id', models.IntegerField()),
                ('viewed', models.IntegerField()),
                ('delivery_charge', models.FloatField()),
                ('delivery_date', models.DateField()),
                ('delivery_time', models.CharField(max_length=100)),
                ('delivery_asap', models.CharField(max_length=14)),
                ('delivery_instruction', models.CharField(max_length=255)),
                ('voucher_code', models.CharField(max_length=100)),
                ('voucher_amount', models.FloatField()),
                ('voucher_type', models.CharField(max_length=100)),
                ('cc_id', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
                ('ip_address', models.CharField(max_length=50)),
                ('order_change', models.FloatField()),
                ('payment_provider_name', models.CharField(max_length=255)),
                ('discounted_amount', models.FloatField()),
                ('discount_percentage', models.FloatField()),
                ('percent_commision', models.FloatField()),
                ('total_commission', models.FloatField()),
                ('commision_ontop', models.IntegerField()),
                ('merchant_earnings', models.FloatField()),
                ('packaging', models.FloatField()),
                ('cart_tip_percentage', models.FloatField()),
                ('cart_tip_value', models.FloatField()),
                ('card_fee', models.FloatField()),
                ('donot_apply_tax_delivery', models.IntegerField()),
                ('order_locked', models.IntegerField()),
                ('request_from', models.CharField(max_length=10)),
                ('mobile_cart_details', models.TextField(blank=True, null=True)),
                ('points_discount', models.FloatField()),
                ('apply_food_tax', models.IntegerField()),
                ('order_id_token', models.CharField(max_length=100)),
                ('admin_viewed', models.IntegerField()),
                ('merchantapp_viewed', models.IntegerField()),
                ('dinein_number_of_guest', models.CharField(max_length=14)),
                ('dinein_special_instruction', models.CharField(max_length=255)),
                ('critical', models.IntegerField()),
                ('commision_type', models.CharField(max_length=50)),
                ('request_cancel', models.IntegerField()),
                ('request_cancel_viewed', models.IntegerField()),
                ('request_cancel_status', models.CharField(max_length=255)),
                ('sofort_trans_id', models.CharField(max_length=255)),
                ('calculation_method', models.IntegerField()),
                ('dinein_table_number', models.CharField(max_length=50)),
                ('new_delivery_time', models.TimeField(blank=True, null=True)),
                ('cancel_reason', models.TextField(blank=True, null=True)),
                ('payment_gateway_ref', models.CharField(max_length=255)),
                ('distance', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'mt_order',
                'managed': False,
            },
        ),
    ]