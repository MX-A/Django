# Generated by Django 2.2.3 on 2019-09-07 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s821',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]