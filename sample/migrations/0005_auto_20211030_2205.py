# Generated by Django 3.1.4 on 2021-10-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0004_auto_20211030_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlist',
            name='address',
            field=models.TextField(default='Something'),
        ),
    ]