# Generated by Django 4.1.7 on 2023-05-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beyondnatureapp', '0003_overview_image_alter_overview_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overview',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]
