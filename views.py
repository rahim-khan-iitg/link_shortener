from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from . import models,forms
import random
@csrf_exempt
def random_text():
    text="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*=+?.;:"
    id=""
    for i in range(6):
        id=id+random.choice(text)
    return id
@csrf_exempt
def shortener(request):
    login_label="Log In"
    login_link="login"
    if request.user.is_authenticated:
        login_label="Log Out"
        login_link="logout"
    if request.method=="POST":
        form=forms.link_form(request.POST)
        if form.is_valid():
            link=form.cleaned_data['link']
            random_txt=random_text()
            while models.link_db.objects.check(link_id=random_txt):
                random_txt=random_text()
            p=models.link_db(link=link,link_id=random_txt)
            p.save()
            return render(request,"link.html",{"form":forms.link_form,"shorten":"https://rahim-khan.azurewebsites.net/shortener/s/"+random_txt,"original":link,"login_label":login_label,"url":login_link})
        return HttpResponse("thanks")
    return render(request,'link.html',{"form":forms.link_form,"login_label":login_label,"url":login_link})

@csrf_exempt
def urlRedirect(request,slug):
    login_label="Log In"
    login_link="login"
    if request.user.is_authenticated:
        login_label="Log Out"
        login_link="logout"
    if models.link_db.objects.check(link_id=slug):
        data=models.link_db.objects.get(link_id=slug)
        return redirect(data.link)
    return render(request,"broken_link.html",{"login_label":login_label,"url":login_link})