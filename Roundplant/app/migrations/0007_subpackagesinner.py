# Generated by Django 4.2.7 on 2024-01-16 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_subpackages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subpackagesinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Duration', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=50)),
                ('Price', models.CharField(max_length=50)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.packages')),
            ],
        ),
    ]
