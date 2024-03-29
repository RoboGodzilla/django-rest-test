# Generated by Django 4.1.2 on 2022-10-17 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pallet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.IntegerField()),
                ('is_empty', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('max_racks_qty', models.IntegerField()),
                ('max_total_weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodegas.level')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('max_weight', models.IntegerField()),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodegas.space')),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodegas.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='PalletProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('pallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodegas.pallet')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.product')),
            ],
        ),
        migrations.AddField(
            model_name='pallet',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodegas.section'),
        ),
        migrations.AddField(
            model_name='level',
            name='rack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodegas.rack'),
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.product')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodegas.warehouse')),
            ],
        ),
    ]
