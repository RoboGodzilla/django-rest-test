# Generated by Django 4.1.2 on 2022-10-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodegas', '0003_remove_pallet_code_pallet_location_alter_pallet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pallet',
            name='id',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]