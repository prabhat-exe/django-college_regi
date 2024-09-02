from django.shortcuts import render,redirect,get_object_or_404
# from django.http import HttpResponse
from .models import student
import hashlib
from datetime import datetime

def hash_password(password):
    # Encode the password string into bytes
    password_bytes = password.encode('utf-8')
    
    # Apply SHA-256 hashing to the password bytes
    hashed_bytes = hashlib.sha256(password_bytes)
    
    # Get the hexadecimal representation of the hashed bytes
    hashed_password = hashed_bytes.hexdigest()
    
    return hashed_password




# Create your views here.
def index(req):
    return render(req,'index.html')

def signup(req):
    if req.method == 'POST':
        name = req.POST.get('name').title()   # Get the value of 'name' field from POST data
        fname=req.POST.get('fathername').title()
        email = req.POST.get('email')
        phone=req.POST.get('phone')
        p=req.POST.get('password')
        password=hash_password(p)
        cp=req.POST.get('cpassword')
        cpassword=hash_password(cp)
        crtd=datetime.today()
        date="%s/%s/%s" % (crtd.day,crtd.month,crtd.year)
        # print(name,fname,email,phone,password,cpassword)
        if (password==cpassword):
            obj=student(name=name,fname=fname,email=email,phone=phone,password=password,dt=str(date))
            obj.save()
        else:
            print("check the password!!!!!")
    return render(req,'signup.html')

def login(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        p=req.POST.get('password')
        password=hash_password(p)
        obj=student.objects.get(email=email)
        if email==obj.email and password == obj.password:
                print(obj.email,obj.password)
                req.session['email']=email
                return redirect('details')
        else:
            return render(req,'login.html')
    return render(req,'login.html')

def details(req):
    e=req.session.get('email')
    i=student.objects.get(email=e)
    return render(req,'details.html',{'student':i})

def cpass(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        f=req.POST.get('Fname')
        obj=student.objects.get(email=e)
        req.session['email']=e
        if e==obj.email and f==obj.fname:
            return redirect('change')
        else:
            return render(req,'cpass.html')
    return render(req,'cpass.html')

def change(req):
     if req.method == 'POST':
         e=req.session.get('email')
         password=req.POST.get('password')
         cpassword=req.POST.get('cpassword')
         obj=student.objects.get(email=e)
         print(obj)
         if(password==cpassword):
             p=hash_password(password)
             obj=student(password=p)
             obj.save()
         else:
            print('the passwoed was not matching!!!')
     return render(req,'change.html')
