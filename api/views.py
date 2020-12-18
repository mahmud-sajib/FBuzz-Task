import requests
import datetime
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import InfoUpload, CvFileUpload, ApiToken, CvFileToken
from .forms import InfoUploadForm, CvFileUploadForm

# Create your views here.

"""This function handles authentication of a user."""
def login_view(request):
    
    if request.method == 'POST':
        # Get user email and password 
        email = request.POST.get('email')
        password = request.POST.get('password')

        # POST auth information to api 3.1
        url = "https://recruitment.fisdev.com/api/login/"
        payload = {'username': email, 'password': password}
        response = requests.post(url, data=payload)
        
        # Get response in json format
        response = response.json()

        # If it's a valid response save token and redirect user else show error message
        if response["success"] == True:
            ApiToken.objects.create(api_token=response["token"])
            return redirect('info-upload')    
        else:
            messages.error(request, 'Invalid credentials. Please enter correct username or password.')

    return render(request, 'api/index.html')

"""This function handles information upload of a user."""
def info_upload_view(request):
    
    form = InfoUploadForm(request.POST or None)
    
    # If information is valid save the form else show error message
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            # Instantiate info object
            info_obj = InfoUpload.objects.latest('on_spot_creation_time')

            # Convert cv_file object into a JSON object  
            cv_tsync_id = info_obj.cv_file_tsync_id
            cv_file = {
                "tsync_id": f"{cv_tsync_id}"
            }
            cv_file_json = json.loads(json.dumps(cv_file))
            
            # Assign api payload values 
            payload = {
                "tsync_id": str(info_obj.tsync_id), 
                "name": info_obj.name,
                "email": info_obj.email,     
                "phone": info_obj.phone,     
                "full_address": info_obj.full_address,     
                "name_of_university": info_obj.name_of_university,     
                "graduation_year": info_obj.graduation_year,     
                "cgpa": info_obj.cgpa,     
                "experience_in_months": info_obj.experience_in_months,     
                "current_work_place_name": info_obj.current_work_place_name,     
                "applying_in": info_obj.applying_in,     
                "expected_salary": info_obj.expected_salary,     
                "field_buzz_reference": info_obj.field_buzz_reference,     
                "github_project_url": info_obj.github_project_url,
                "cv_file": cv_file_json,
                "on_spot_update_time": int(info_obj.on_spot_update_time.timestamp()),
                "on_spot_creation_time": int(info_obj.on_spot_creation_time.timestamp()) 
            }

            # Get authorization token
            token_obj = ApiToken.objects.latest('api_token')
            api_token_key = token_obj.api_token
            auth_headers = {
                "Authorization": f"Token {api_token_key}"
            }

            # POST user information to api 3.2
            url = "https://recruitment.fisdev.com/api/v0/recruiting-entities/"
            response = requests.post(url, json=payload, headers=auth_headers)
            
            # Get response in json format
            response = response.json()

            # If it's a valid response save file token and redirect user else show error message
            if response["success"] == True:
                CvFileToken.objects.create(cv_token=response["cv_file"]["id"])
                return redirect('cv-upload')    
            else:
                messages.error(request, 'Invalid credentials. Please enter correct username or password.')
        else:
            messages.error(request, 'One or more fields have an error. Please provide valid information.')
    else:
        form = InfoUploadForm()
        
    context = {
        'form': form
    }
    
    return render(request, 'api/info-upload.html', context)

"""This function handles cv upload of a user."""
def cv_file_upload_view(request):

    cv_form = CvFileUploadForm(request.POST, request.FILES)
    
    # If information is valid save the form else show error message
    if request.method == 'POST':
        if cv_form.is_valid():
            cv_form.save()

            # Open binary cv file
            cv_obj = CvFileUpload.objects.latest('document')
            cv_file = cv_obj.document.path
            files = {'file': open(cv_file, 'rb')}

            # Get cv file token id
            cv_token_obj = CvFileToken.objects.latest('cv_token')
            FILE_TOKEN_ID = cv_token_obj.cv_token
            url = f'https://recruitment.fisdev.com/api/file-object/{FILE_TOKEN_ID}/'

            # Get authorization token
            token_obj = ApiToken.objects.latest('api_token')
            api_token_key = token_obj.api_token
            auth_headers = {
                "Authorization": f"Token {api_token_key}"
            }
            
            # PUT user CV to api 3.3
            response = requests.put(url, files=files, headers=auth_headers)

            # Get response in json format
            response = response.json()
            print(response)

            # If it's a valid response save file token and redirect user else show error message
            if response["success"] == True:
                messages.success(request, 'Congrats! You have successfully submited all information.')  
            else:
                messages.error(request, 'Invalid credentials. Please enter correct username or password.')
    else:
        cv_form = CvFileUploadForm()

    context = {
        'cv_form': cv_form
    }
    
    return render(request, 'api/cv-upload.html', context)
