from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("UserName Taken")
                messages.info(request,"UserName Taken")
                return redirect ('register')
            elif User.objects.filter(email=email).exists():
                print("Email taken")
                messages.info(request,"Email taken")
                return redirect ('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)  # query(ORM) to save data in postgreSql database
                user.save()
        else:
            print("Password are not matching")
            messages.info(request,"Password are not matching")
            return redirect ('register')

        return redirect('/')
    else:
        return render(request,'register.html')
