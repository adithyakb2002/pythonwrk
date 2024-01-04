# Generated by Django 3.2.12 on 2024-01-04 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_ayushsilverplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('heading1', models.CharField(max_length=255)),
                ('heading2', models.CharField(max_length=255)),
                ('heading3', models.CharField(max_length=255)),
                ('paragraph2', models.CharField(max_length=255)),
                ('paragraph3', models.CharField(max_length=255)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.blog')),
            ],
        ),
    ]
