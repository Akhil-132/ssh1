# Generated by Django 4.1 on 2023-06-06 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beyondnatureapp', '0022_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('text', models.TextField(max_length=30)),
                ('address', models.TextField(max_length=30)),
            ],
        ),
    ]
