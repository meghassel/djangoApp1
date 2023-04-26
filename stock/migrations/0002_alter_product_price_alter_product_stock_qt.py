# Generated by Django 4.1.8 on 2023-04-26 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_qt',
            field=models.IntegerField(max_length=5, null=True),
        ),
    ]
