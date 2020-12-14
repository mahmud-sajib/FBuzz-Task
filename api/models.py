import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django_unixdatetimefield import UnixDateTimeField
import datetime

# Create your models here.

class InfoUpload(models.Model):

    APPLYING_DEPARTMENT = (
        ('MOBILE', 'Mobile'),
        ('BACKEND', 'Backend'),
    )
    
    tsync_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    name = models.CharField(max_length=256)
    
    email = models.EmailField(max_length=256) # validation required
    
    phone = models.CharField(max_length=14) # validation required
    
    full_address = models.TextField(max_length=512, blank=True)
    
    name_of_university = models.CharField(max_length=256)
    
    graduation_year = models.IntegerField(validators=[
        MinValueValidator(2015),
        MaxValueValidator(2020)
    ], default=2020)
    
    cgpa = models.FloatField(validators=[
        MinValueValidator(2.0),
        MaxValueValidator(4.0)
    ], blank=True)
    
    experience_in_months = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ], default=12, blank=True)

    current_work_place_name = models.CharField(max_length=256, blank=True)

    applying_in = models.CharField(choices=APPLYING_DEPARTMENT, max_length=14, default=APPLYING_DEPARTMENT[1][1])

    expected_salary = models.IntegerField(validators=[
        MinValueValidator(15000),
        MaxValueValidator(60000)
    ], default=30000)

    field_buzz_reference = models.CharField(max_length=256, blank=True)

    github_project_url = models.URLField(max_length=512)
    
    cv_file_tsync_id = models.UUIDField(default=uuid.uuid4, editable=False)
    
    on_spot_update_time = UnixDateTimeField(auto_now=True, editable=False)
 
    on_spot_creation_time = UnixDateTimeField(auto_now_add=True, editable=False)

    # def save(self, *args, **kwargs):
    #     self.on_spot_creation_time = datetime.datetime.now().timestamp()
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# class CvFile(models.Model):
#     tsync_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

#     def __str__(self):
#         return self.tsync_id









