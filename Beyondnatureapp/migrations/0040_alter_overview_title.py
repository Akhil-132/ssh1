# Generated by Django 4.2.1 on 2023-06-08 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beyondnatureapp', '0039_remove_overview_webp_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overview',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]