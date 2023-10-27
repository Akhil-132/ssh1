# Generated by Django 4.1 on 2023-06-06 13:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beyondnatureapp', '0030_alter_enquire_now_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquire_now',
            name='Mobile_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator('^[0-9+]', 'only digit characters.')]),
        ),
    ]
