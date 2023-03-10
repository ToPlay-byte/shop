# Generated by Django 4.1.1 on 2023-02-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantity'),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=20.0, max_digits=10, verbose_name='Total price'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
