# Generated by Django 5.0 on 2023-12-13 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mncmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ceo', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('Industry', models.CharField(max_length=100)),
            ],
        ),
    ]
