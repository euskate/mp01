# Generated by Django 3.0.2 on 2020-01-28 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0003_continentname'),
    ]

    operations = [
        migrations.AddField(
            model_name='countryname',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]