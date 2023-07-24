# Generated by Django 3.2.12 on 2023-07-18 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank='false', max_length=30, null='false')),
                ('school', models.CharField(blank='false', max_length=30, null='false')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]