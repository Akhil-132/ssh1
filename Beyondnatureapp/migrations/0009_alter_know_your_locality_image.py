# Generated by Django 4.1 on 2023-05-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beyondnatureapp', '0008_enquire_now_enquiry_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='know_your_locality',
            name='image',
            field=models.ImageField(upload_to='locality_images'),
        ),
    ]
