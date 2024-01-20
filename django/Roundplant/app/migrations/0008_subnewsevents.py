# Generated by Django 4.2.7 on 2024-01-19 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_subpackagesinner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subnewsevents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('paragraph', models.TextField()),
                ('images', models.ImageField(upload_to='img')),
                ('description', models.CharField(max_length=50)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.packages')),
            ],
        ),
    ]