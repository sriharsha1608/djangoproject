# Generated by Django 3.1.4 on 2020-12-10 08:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Branch_code', models.CharField(max_length=300, unique=True)),
                ('Branch_Name', models.CharField(max_length=300)),
                ('Branch_Addres', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('Item_Name', models.CharField(max_length=300, null=True, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transactions_ID', models.CharField(blank=True, default=uuid.uuid4, max_length=100, null=True, unique=True)),
                ('Item_Id', models.IntegerField()),
                ('Source_Branch', models.CharField(max_length=300)),
                ('Destination_Branch', models.CharField(max_length=300)),
                ('Quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_Quantity', models.IntegerField()),
                ('Item_Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Qt.item')),
            ],
        ),
    ]