# Generated by Django 4.1.1 on 2023-02-22 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_alter_order_created_alter_order_post_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 2, 22, 12, 31, 5, 687769, tzinfo=datetime.timezone.utc), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='order',
            name='post_code',
            field=models.PositiveIntegerField(verbose_name='Post code'),
        ),
    ]
