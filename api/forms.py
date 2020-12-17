from django import forms
from .models import InfoUpload, CvFileUpload

class InfoUploadForm(forms.ModelForm):
    class Meta:
        model = InfoUpload
        fields = '__all__'

class CvFileUploadForm(forms.ModelForm):
    class Meta:
        model = CvFileUpload
        fields = '__all__'