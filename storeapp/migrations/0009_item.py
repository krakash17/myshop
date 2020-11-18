# Generated by Django 3.1 on 2020-11-01 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0008_auto_20201101_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_id', models.IntegerField()),
                ('item_name', models.CharField(max_length=30, unique=True)),
                ('item_description', models.CharField(max_length=75, unique=True)),
                ('item_price', models.IntegerField()),
                ('item_amount', models.IntegerField(default=0)),
                ('item_flag', models.BooleanField()),
                ('item_quantity', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]