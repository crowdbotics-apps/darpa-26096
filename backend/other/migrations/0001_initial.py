# Generated by Django 2.2.19 on 2021-05-03 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foreign_Asset1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.BigIntegerField()),
                ('location', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Foreign_Asset2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.BigIntegerField()),
                ('location', models.BigIntegerField()),
            ],
        ),
    ]