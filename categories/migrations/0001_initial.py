# Generated by Django 3.2.9 on 2021-11-23 01:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('color', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(message='Cor inválida', regex='^#(?:[0-9a-fA-F]{3}){2}$')])),
                ('priority', models.PositiveIntegerField(blank=True)),
            ],
            options={
                'ordering': ['priority'],
            },
        ),
    ]
