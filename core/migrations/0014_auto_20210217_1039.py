# Generated by Django 3.1.6 on 2021-02-17 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_order_billing_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='countries',
            new_name='country',
        ),
    ]
