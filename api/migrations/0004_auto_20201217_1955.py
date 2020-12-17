# Generated by Django 3.1 on 2020-12-17 13:55

import api.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201217_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvfileupload',
            name='document',
            field=models.FileField(upload_to='documents/', validators=[api.validators.validate_file_size, django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
