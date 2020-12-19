import uuid
import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, FileExtensionValidator
from django_unixdatetimefield import UnixDateTimeField
from .validators import validate_file_size

# Create your models here.

"""ApiToken model"""
class ApiToken(models.Model):
    api_token = models.CharField(max_length=256, editable=False)
    
    def __str__(self):
        return self.api_token

"""InfoUpload model"""
class InfoUpload(models.Model):

    APPLYING_DEPARTMENT = (
        ('MOBILE', 'Mobile'),
        ('BACKEND', 'Backend'),
    )
    
    tsync_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=55)
    
    name = models.CharField(max_length=256)
    
    email = models.EmailField(max_length=256)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{11,13}$', message="Phone number must be in digit. Min 11 and Max 14 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=14, help_text='You can use a country code e.g. +880 (optional)')
    
    full_address = models.TextField(max_length=512, blank=True)
    
    name_of_university = models.CharField(max_length=256)
    
    graduation_year = models.IntegerField(validators=[
        MinValueValidator(2015),
        MaxValueValidator(2020)
    ], default=2020, help_text = "Value must be from 2015 to 2020")
    
    cgpa = models.FloatField(validators=[
        MinValueValidator(2.0),
        MaxValueValidator(4.0)
    ], default=3.0, blank=True, help_text = "Value must be from 2.0 to 4.0")
    
    experience_in_months = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ], default=12, blank=True, help_text = "Value Must be from 0 to 100 (in months)")

    current_work_place_name = models.CharField(max_length=256, blank=True)

    applying_in = models.CharField(choices=APPLYING_DEPARTMENT, max_length=14, default=APPLYING_DEPARTMENT[1][1])

    expected_salary = models.IntegerField(validators=[
        MinValueValidator(15000),
        MaxValueValidator(60000)
    ], default=30000, help_text = "Value must be from 15000 to 60000")

    field_buzz_reference = models.CharField(max_length=256, blank=True)

    github_project_url = models.URLField(max_length=512)
    
    cv_file_tsync_id = models.UUIDField(default=uuid.uuid4, editable=False, max_length=55)
    
    on_spot_update_time = UnixDateTimeField(auto_now=True, editable=False)
 
    on_spot_creation_time = UnixDateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

"""CvFileToken model"""
class CvFileToken(models.Model):
    cv_token = models.CharField(max_length=256, editable=False)
    
    def __str__(self):
        return self.cv_token

"""CvFileUpload model"""
class CvFileUpload(models.Model):
    document = models.FileField(upload_to='documents/', validators=[validate_file_size, FileExtensionValidator(allowed_extensions=['pdf'])])

    def __str__(self):
        return f"Cv File"









