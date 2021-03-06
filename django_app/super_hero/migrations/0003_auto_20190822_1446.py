# Generated by Django 2.2.4 on 2019-08-22 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_hero', '0002_auto_20190822_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street_name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='gender',
            name='name',
            field=models.CharField(max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='full_name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='power',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
