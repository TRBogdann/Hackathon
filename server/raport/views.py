from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from django import forms
from .models import Users
from .models import raport


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['user_id','username','password']

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
        form = raport(request.POST)
        fk_id = raport.objects.get(username=form.data['username'])
        newId = raport.objects.count()+1
        data = form.data.copy()
        data['raport_id']=newId
        data['user_id']= fk_id.id
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
def log_usr(request):
    if(request.method=='POST'):
        form = UserForm(request.POST)
        check1=Users.objects.filter(username=form.data['username']).exists()
        check2=Users.objects.filter(password=form.data['password']).exists()
        if check1 and check2:
            session_id = get_random_string(42)
            return JsonResponse({'session_id':session_id})

        else:
            return JsonResponse({'message': 'not Valid'})

    else:
        print("Not Working")
        return HttpResponse("Nothing Here")


