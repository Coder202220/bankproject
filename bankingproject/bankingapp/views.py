from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import Apply
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('applybutton')
        else:
            messages.info(request,"invalid credentials")
            return redirect('/')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['cpassword']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request ,"username already taken")
                return HttpResponseRedirect('message')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login/')

        else:
            messages.info(request,"password not matching")
            return redirect('register')

    return render(request,"register.html")

def applybutton(request):
    return render(request,"applybutton.html")


def applyform(request):
    if request.method=='POST':
        name1=request.POST.get('name')
        dob1=request.POST.get('date')
        gender1 = request.POST.get('gender')
        age1 = request.POST.get('age')
        phone1 = request.POST.get('phone')
        mail = request.POST.get('Email')
        address1 = request.POST.get('address')
        district1 = request.POST.get('district')
        branch1 = request.POST.get('branch')
        acc_type = request.POST.get('accounts')
        material1 = request.POST.get('materials')
        apply1=Apply(name=name1,dob=dob1,age=age1,gender=gender1,phoneno=phone1,mailid=mail,
                  address=address1,district=district1, branch=branch1,account_type=acc_type,
                  material=material1)
        apply1.save()
    else:
        print("invalid entry")
    return render(request,"applyform.html")

# def message1(request):
#     render(request,"message.html")

def logout(request):
    auth.logout(request)
    return redirect('/')