import sys
sys.setrecursionlimit(10000)
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseNotFound
# Create your views here.
from django.shortcuts import render
import datetime
from .models import tb_registration, emp_model
from .form import RegistrationForm1
from .form import login, emp1

today=datetime.datetime.now()
def hello(request):
    text="<h1>welcome to django</h1>"
    return HttpResponse(text)


#connect with a template
def temp(request):
    return render(request,"sapp/base.html")
def mypage(request):
    return render(request,"sapp/mypage.html",{'name':'shubham_bajaj','today':today})
def demo(request):
    list=["pen","pencil","notebook"]
    uname=none
    return render(request, "sapp/mypage.html", {'person_name': uname, 'ship_date': today,"item_list":item_list})
def img(request):
    return render(request,"sapp/index.html")
def register(request):
    if request.method=='POST':
       # form = UserCreationForm(request.POST)
        form = RegistrationForm1(request.POST)
        if form.is_valid():
            name1 = form.cleaned_data["name"]
            email1 = form.cleaned_data["email"]
            contact1 = form.cleaned_data["contact"]
            address1 = form.cleaned_data["address"]
            password1 = form.cleaned_data["password"]
            gender1 = form.cleaned_data["Gender"]
            print("1111111111")
            p = tb_registration(name = name1, email = email1, contact = contact1, address=address1, password = password1, gender = gender1)
            print(p)
            p.save()
            print("\n\n this is valid data from the form ",gender1)
            return render(request,"sapp/info.html",{'name':name1,'email':email1,'address':address1,'contact':contact1})
        else:
            #form = UserCreationForm()
            #args = {'form':form}
            print("2222222222")
            return render(request,"sapp/form.html" ,{'form':form})
    else:
        form = RegistrationForm1()

        #args = form                    print("valid user",p)

        print("2333333333")
        return render(request,"sapp/form.html", {'form':form})

def logedin(request):
    if request.method == 'POST':
        form = login(request.POST)

        if form.is_valid():
            u_email = form.cleaned_data["email"]
            u_password = form.cleaned_data["password"]
            p = tb_registration.objects.filter(email=u_email,password=u_password)
            print(p)

            if (p.count()>0):
                request.session[ 'username' ] = u_email
                if request.session.has_key('username'):
                    u_name = request.session['username']
                    print(u_name)
                    print(p[0].name)

                return HttpResponseRedirect("/welcome/thanks")
            else:
                print("try again user")
                return HttpResponseNotFound('<h1>no page found</h1>')

        else:
              print('\n\n this is else block:{0}\n\n')
              return render(request,"sapp/login.html",{'form': form })
    else:
        form = login()
        return render(request, "sapp/login.html", {'form': form})

def thanks(request):
    return render(request,"sapp/thanks.html")

def emp(request):
    if request.method == 'POST':
        form = emp1(request.POST)
        if form.is_valid():
            if request.session.has_key('username'):
                email1 = request.session['username']
            r= tb_registration.objects.get(email=email1)


            salary = form.cleaned_data["e_salary"]
            experience = form.cleaned_data["e_experience"]
            profile = form.cleaned_data["e_profile"]
            z=emp_model(e_salary=salary,e_experience=experience,e_profile=profile,e_detail=r)
            z.save()
            return render(request, "sapp/thanks.html", {'user':r.first(), 'emp_detail': z})
        else:
            return HttpResponse("Invalid credentials")
    else:
        form = emp1()
        return render(request, 'sapp/emp.html', {'form': form})
