# Generated by Django 4.2.7 on 2024-01-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_newsevents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='img')),
            ],
        ),
    ]
