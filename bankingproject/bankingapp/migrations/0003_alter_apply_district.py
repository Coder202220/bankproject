# Generated by Django 3.2.18 on 2023-03-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0002_auto_20230327_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='district',
            field=models.IntegerField(),
        ),
    ]