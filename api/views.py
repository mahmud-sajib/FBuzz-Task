import requests
import datetime
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import InfoUpload, CvFileUpload
from .forms import InfoUploadForm, CvFileUploadForm

# Create your views here.

# Authentication Token API View
def login_view(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        payload = {'username': email, 'password': password}
        r = requests.post("https://recruitment.fisdev.com/api/login/", data=payload)
        a = r.json()

        if a["success"] == True:
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please enter correct username or password.')

    return render(request, 'api/login.html')

def info_upload_view(request):

    form = InfoUploadForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InfoUploadForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'api/index.html', context)

def info_show(request):
    obj = InfoUpload.objects.latest('on_spot_creation_time')
    print(obj.name)

    cv_file = {
        "tsync_id": "be96f0e188a6de73b186c043-7365-4605-85eb-76021f16803f"
    }

    jsonData = json.loads(json.dumps(cv_file))
    print(type(jsonData))

    payload = {
        "tsync_id": str(obj.tsync_id), 
        "name": obj.name,
        "email": obj.email,     
        "phone": obj.phone,     
        "full_address": obj.full_address,     
        "name_of_university": obj.name_of_university,     
        "graduation_year": obj.graduation_year,     
        "cgpa": obj.cgpa,     
        "experience_in_months": obj.experience_in_months,     
        "current_work_place_name": obj.current_work_place_name,     
        "applying_in": obj.applying_in,     
        "expected_salary": obj.expected_salary,     
        "field_buzz_reference": obj.field_buzz_reference,     
        "github_project_url": obj.github_project_url,
        "cv_file": jsonData,
        "on_spot_update_time": int(obj.on_spot_update_time.timestamp()),
        "on_spot_creation_time": int(obj.on_spot_creation_time.timestamp()) 
    }

    ### Only double quotes are valid in json

    print(payload)
    
    auth_headers = {
        "Authorization": "Token bee247f2f6df8372ff742011aa34e55349552769"
    }

    r = requests.post("https://recruitment.fisdev.com/api/v0/recruiting-entities/", json=payload, headers=auth_headers)

    
    print(r)
    print(r.status_code)
    print(r.json())

    return render(request, 'api/info.html')

def cv_file_upload(request):
    if request.method == 'POST':
        cv_form = CvFileUploadForm(request.POST, request.FILES)
        if cv_form.is_valid():
            cv_form.save()
            return redirect('home')
    else:
        cv_form = CvFileUploadForm()

    context = {
        'cv_form': cv_form
    }
    
    return render(request, 'api/cv-upload.html', context)

def cv_upload_success(request):
    obj = CvFileUpload.objects.latest('document')
    cv_file = obj.document.path

    FILE_TOKEN_ID = 583
    auth_headers = {
        "Authorization": "Token bee247f2f6df8372ff742011aa34e55349552769"
    }
    
    url = f'https://recruitment.fisdev.com/api/file-object/{FILE_TOKEN_ID}/'
    print(f"My url: {url}")
    files = {'file': open(cv_file, 'rb')}

    r = requests.put(url, files=files, headers=auth_headers)

    print(r)
    print(r.status_code)
    print(r.json())

    return render(request, 'api/cv-upload-success.html')
