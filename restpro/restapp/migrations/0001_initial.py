# Generated by Django 4.2.7 on 2023-11-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='restuarant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('foodordered', models.CharField(max_length=100)),
                ('favouritedish', models.CharField(max_length=100)),
                ('review', models.CharField(max_length=500)),
            ],
        ),
    ]
