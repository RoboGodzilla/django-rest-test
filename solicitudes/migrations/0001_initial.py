# Generated by Django 4.1.2 on 2022-10-17 17:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bodegas', '0001_initial'),
        ('entidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motive', models.CharField(max_length=200)),
                ('movement', models.IntegerField()),
                ('approved', models.BooleanField(default=False)),
                ('canceled', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.customer')),
            ],
        ),
        migrations.CreateModel(
            name='RequestProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.product')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.request')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='products',
            field=models.ManyToManyField(through='solicitudes.RequestProduct', to='entidades.product'),
        ),
        migrations.CreateModel(
            name='OutputWarehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('number', models.IntegerField()),
                ('comments', models.CharField(blank=True, max_length=200, null=True)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.request')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodegas.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='OutputPalletProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('output', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.outputwarehouse')),
                ('pallet_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodegas.palletproduct')),
            ],
        ),
        migrations.CreateModel(
            name='InputWarehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('number', models.IntegerField()),
                ('comments', models.CharField(blank=True, max_length=200, null=True)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.request')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodegas.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='InputPalletProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('input', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.inputwarehouse')),
                ('pallet_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodegas.palletproduct')),
            ],
        ),
    ]
