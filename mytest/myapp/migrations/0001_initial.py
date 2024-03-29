# Generated by Django 2.2.3 on 2019-09-07 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('image_path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='s821',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('UA', models.FloatField()),
                ('UB', models.FloatField()),
                ('UC', models.FloatField()),
                ('IA', models.FloatField()),
                ('IB', models.FloatField()),
                ('IC', models.FloatField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='test_tbl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('tem', models.IntegerField()),
                ('Delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='test1_tbl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('sdate', models.DateTimeField()),
                ('stem', models.IntegerField()),
                ('sdelete', models.BooleanField(default=False)),
                ('stest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.test_tbl')),
            ],
        ),
    ]
