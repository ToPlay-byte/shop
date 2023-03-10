# Generated by Django 4.1.1 on 2023-02-28 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25, unique=True, verbose_name='Full name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Contacts',
            },
        ),
    ]
