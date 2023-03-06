from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Reviews ,Food ,Customer
from .forms import Newreviews ,Newfood ,Newcusto, NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.forms import AuthenticationForm #add this

# Create your views here.

def func(req):
    a = loader.get_template('first.html')
    b = Reviews.objects.all().values()
    c = Food.objects.all().values()
    d = Customer.objects.all().values()
    e = {
        'view':b,
        'food':c,
        'Custo':d
    }
    return render(req ,'first.html' ,e)

def func1(req):
    if req.method =='POST':
        abc = Newreviews(req.POST ,req.FILES)

        if abc.is_valid():
            abc.save()
            return redirect('func')

        else:
            return HttpResponse('you Entered Wrong Data')

    else:
        func1 = Newreviews()
        return render(req ,'second.html' ,{'views':func1})

def func2(req ,u_id):
    abc = int(u_id)
    u_sel = Reviews.objects.get(id = abc)
    u_form = Newreviews(req.POST or None, instance=u_sel)

    if u_form.is_valid():
        u_form.save()
        return redirect('func')
    
    return render(req ,'second.html' ,{'views':u_form})

def func3(req ,d_id):
    d_id = int(d_id)
    d_sel = Reviews.objects.get(id = d_id)
    d_sel.delete()
    return redirect('func')


def func4(req):
    if req.method =='POST':
        abc = Newcusto(req.POST ,req.FILES)

        if abc.is_valid():
            abc.save()
            return redirect('func')

        else:
            return HttpResponse('you Entered Wrong Data')

    else:
        func1 = Newcusto()
        return render(req ,'second.html' ,{'views':func1})


def func5(req ,u_id):
    abc = str(u_id)
    u_sel = Customer.objects.get(Customer_Name=abc)
    u_form = Newcusto(req.POST or None, instance=u_sel)

    if u_form.is_valid():
        u_form.save()
        return redirect('func')
    
    return render(req ,'second.html' ,{'views':u_form})

def func6(req ,d_id):
    d_id = str(d_id)
    d_sel = Customer.objects.get(Customer_Name = d_id)
    d_sel.delete()
    return redirect('func')


def func7(req):
    if req.method =='POST':
        abc = Newfood(req.POST ,req.FILES)

        if abc.is_valid():
            abc.save()
            return redirect('func')

        else:
            return HttpResponse('you Entered Wrong Data')

    else:
        func1 = Newfood()
        return render(req ,'second.html' ,{'views':func1})

def func8(req ,u_id):
    abc = str(u_id)
    u_sel = Food.objects.get(Food_Name = abc)
    u_form = Newfood(req.POST or None, instance=u_sel)

    if u_form.is_valid():
        u_form.save()
        return redirect('func')
    
    return render(req ,'second.html' ,{'views':u_form})

def func9(req ,d_id):
    d_id = str(d_id)
    d_sel = Food.objects.get(Food_Name = d_id)
    d_sel.delete()
    return redirect('func')


def login_request(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request ,request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username =username,password=password)
        
            if user is not None:
                login(request,user)
                return redirect('func')
            else:
                return HttpResponse('Invalid Username or Password')
        else:
            return HttpResponse('Invalid Username or Password')

    login_form = AuthenticationForm()
    return render(request,'login.html', {'login':login_form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("func")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request,"register.html",{"register":form})


