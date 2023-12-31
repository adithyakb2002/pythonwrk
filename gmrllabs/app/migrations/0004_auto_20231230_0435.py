# Generated by Django 3.2.12 on 2023-12-30 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
