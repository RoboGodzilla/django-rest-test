# Generated by Django 4.1.2 on 2022-10-24 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodegas', '0002_alter_inventory_customer_alter_inventory_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pallet',
            name='code',
        ),
        migrations.AddField(
            model_name='pallet',
            name='location',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pallet',
            name='id',
            field=models.CharField(editable=False, max_length=12, primary_key=True, serialize=False),
        ),
    ]
