# Generated by Django 2.2.4 on 2019-08-22 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_hero', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='power',
        ),
        migrations.AddField(
            model_name='hero',
            name='power',
            field=models.ManyToManyField(related_name='heroes', to='super_hero.Power'),
        ),
    ]
