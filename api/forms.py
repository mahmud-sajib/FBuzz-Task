from django import forms
from .models import InfoUpload, CvFileUpload

"""InfoUpload model form"""
class InfoUploadForm(forms.ModelForm):
    class Meta:
        model = InfoUpload
        fields = '__all__'

"""CvFileUpload model form"""
class CvFileUploadForm(forms.ModelForm):
    class Meta:
        model = CvFileUpload
        fields = '__all__'