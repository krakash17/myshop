# Generated by Django 3.1 on 2020-11-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0007_auto_20201031_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategories',
            name='category_id',
            field=models.IntegerField(),
        ),
    ]
