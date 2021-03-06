# Generated by Django 3.1 on 2020-12-17 11:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CvFileToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv_token', models.CharField(editable=False, max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='infoupload',
            name='phone',
            field=models.CharField(help_text='You can use a country code e.g. +880 (optional)', max_length=14, validators=[django.core.validators.RegexValidator(message='Phone number must be in digit. Min 11 and Max 14 digits allowed.', regex='^\\+?1?\\d{11,13}$')]),
        ),
    ]
