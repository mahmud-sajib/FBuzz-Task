from django import forms
from .models import InfoUpload, CvFileUpload

class InfoUploadForm(forms.ModelForm):

    # name = forms.CharField(label="", widget=forms.TextInput(attrs={
    #     'type': 'name',
    #     'class':'form-control form-control-style-3',
    #     'placeholder':'Name',
    # }))

    #  email = forms.EmailField(widget=forms.TextInput(attrs={
    #     'type': 'email',
    #     'class': 'form-control',  
    #     'placeholder': 'Email Address'
    # }))

    # description = forms.CharField(label="", widget=forms.Textarea(attrs={
    #     'class':'form-control form-control-style-3',
    #     'placeholder':'Description in detail...',
    #     'rows':'8',
    #     'cols':'80',
    # }))

    class Meta:
        model = InfoUpload
        fields = '__all__'

class CvFileUploadForm(forms.ModelForm):
    class Meta:
        model = CvFileUpload
        fields = '__all__'