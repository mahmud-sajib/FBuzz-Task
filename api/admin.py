from django.contrib import admin
from .models import InfoUpload

# Register your models here.
class InfoUploadAdmin(admin.ModelAdmin):
    # Display columns in horizontal list
    list_display = ('tsync_id', 'name', 'cv_file_tsync_id', 'on_spot_creation_time', 'on_spot_update_time')

admin.site.register(InfoUpload, InfoUploadAdmin)

# class CvFileAdmin(admin.ModelAdmin):
#     # Display columns in horizontal list
#     list_display = ('tsync_id',)

# admin.site.register(CvFile, CvFileAdmin)

