# Generated by Django 4.1.1 on 2023-02-22 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_alter_order_address_alter_order_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 2, 22, 12, 30, 4, 600572, tzinfo=datetime.timezone.utc), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='order',
            name='post_code',
            field=models.PositiveIntegerField(max_length=18, verbose_name='Post code'),
        ),
    ]
