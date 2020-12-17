from django.contrib import admin
from .models import InfoUpload, CvFileUpload, ApiToken, CvFileToken 

# Register your models here.
class InfoUploadAdmin(admin.ModelAdmin):
    # Display columns in horizontal list
    list_display = ('tsync_id', 'name', 'cv_file_tsync_id', 'on_spot_creation_time', 'on_spot_update_time')

admin.site.register(InfoUpload, InfoUploadAdmin)
admin.site.register(CvFileUpload)
admin.site.register(ApiToken)
admin.site.register(CvFileToken)

