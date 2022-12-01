from django.shortcuts import render
import requests

def index(request): 
    return render(request,'index.html')

def applications(request):
    response = requests.get('https://engineering-task.elancoapps.com/api/applications')
    applications = response.json()
    return render(request,"applications.html",{'applications':applications})

def select_app_name(request,app):
    response = requests.get('https://engineering-task.elancoapps.com/api/applications/'+ app)
    application_Name = response.json()
    return render(request,"appNameResults.html", {'select_app_name':application_Name})
    
def resources(request):    
    response = requests.get('https://engineering-task.elancoapps.com/api/resources')
    resources_details = response.json()
    return render(request,"resources.html", {'resources':resources_details})

def select_resource_name(request,res):
    response = requests.get('https://engineering-task.elancoapps.com/api/resources/'+res)
    resources_name_details = response.json()
    return render(request,"resourceNameResults.html", {'select_resource_name':resources_name_details})


