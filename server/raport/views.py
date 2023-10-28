from django.shortcuts import render

from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from django import forms
from .models import Users
from .models import raport
from .models import UserSession
from django.shortcuts import render
from .weather import general_alert
import string
import random


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['user_id','username','password']

class newSession(forms.ModelForm):
    class Meta:
        model = UserSession
        fields = ['session_id','user_id']

class newData(forms.ModelForm):
    class Meta:
        model = raport
        fields = ['report_id','user_id','lat','lng','strada','path_to_Photo','description']   

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str




@csrf_exempt
def rep_post(request):
    if(request.method=='POST'):
        newId=Users.objects.count()+1
        form = UserForm(request.POST)
        data = form.data.copy()
        data['user_id']=newId
        form.data=data
        if form.is_valid():
            print(form.data)
            form.save()
        
        else:
            print("Not Valid")
            
        
        return JsonResponse({'message': 'done'})
    else:
        print("Not Working")
        return HttpResponse("Nothing Here")

@csrf_exempt
def user_post(request):
    if(request.method=='POST'):
        form = newData(request.POST)
        newId = raport.objects.count()+1
        data = form.data.copy()
        data['report_id']=newId
        print(data)
        form.data=data
        if form.is_valid():
            print(form.data)
            form.save()
            
        return JsonResponse({'message': 'done'})
    else:
        print("Not Working")
        return HttpResponse("Nothing Here")


@csrf_exempt
def log_usr(request):
    if(request.method=='POST'):
        form = UserForm(request.POST)
        check1=Users.objects.filter(username=form.data['username']).exists()
        check2=Users.objects.filter(password=form.data['password']).exists()
        if check1 and check2:
            session_id = get_random_string(42)
            fk_id = Users.objects.filter(username=form.data['username']).first()     
            sessionForm = newSession()
            new_session = sessionForm.save(commit=False)
            new_session.session_id=session_id
            new_session.user_id=fk_id.user_id
            print(new_session)
            new_session.save()
            
            return JsonResponse({'value':{'session_id':session_id,'user_id':fk_id.user_id},'name':'session_id','status':200})

        else:
            return JsonResponse({'message': 'not Valid'})

    else:
        print("Not Working")
        return HttpResponse("Nothing Here")

@csrf_exempt
def view_app(request):
    return render(request,"locatie.html")

@csrf_exempt
def view_finalizare(request):
    element=raport.objects.latest('report_id')
    general_alert(element.strada,element.lat,element.lng)
    
    print(element.lat)
    return render(request,"finalizare.html")
    

