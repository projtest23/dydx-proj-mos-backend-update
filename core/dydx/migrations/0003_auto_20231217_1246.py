# Generated by Django 3.2.23 on 2023-12-17 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dydx', '0002_rename_side_positions_long'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='balance',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='positions',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='positions',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
