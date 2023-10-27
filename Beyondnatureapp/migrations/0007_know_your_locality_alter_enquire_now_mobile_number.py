# Generated by Django 4.1 on 2023-05-10 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beyondnatureapp', '0006_alter_enquire_now_mobile_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='know_your_locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
                ('discription', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='enquire_now',
            name='Mobile_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
