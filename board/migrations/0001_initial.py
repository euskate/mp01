# Generated by Django 3.0.2 on 2020-01-24 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table1',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('writer', models.CharField(max_length=32)),
                ('hit', models.IntegerField()),
                ('b_img', models.BinaryField(null=True)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
