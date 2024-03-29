# Generated by Django 3.2.9 on 2021-11-23 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500)),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('youtube_image', models.URLField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='categories.category')),
            ],
        ),
    ]
