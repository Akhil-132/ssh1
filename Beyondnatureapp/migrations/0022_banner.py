# Generated by Django 4.1 on 2023-06-06 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beyondnatureapp', '0021_configuration1'),
    ]

    operations = [
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner_images')),
            ],
        ),
    ]
