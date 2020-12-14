import requests
from django.shortcuts import render, redirect
from .models import *
from .forms import InfoUploadForm
import datetime
import json

# Create your views here.

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
