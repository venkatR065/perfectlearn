from contact.models import Contact
from django.shortcuts import render
from django.shortcuts import redirect
from contact.models import Email
from courses.models import Service
from courses.models import Course
from courses.models import New


def base(r):
    if r.method == 'POST':
        if r.POST['email'] :
            emails=Email()
            emails.email=r.POST['email']
            
            emails.save()
            return redirect('home')
        else:
            return render(r ,'perfectlearn/base.html',{'error':'all  fiels are required to fill'})

    return render(r ,'perfectlearn/base.html')
    




def home(r):
    courses=Course.objects
    news=New.objects
    
    
    return render(r,'perfectlearn/home.html',{'courses':courses,'news':news})
def cont(r):
   if r.method == 'POST':
        if r.POST['Name'] and r.POST['email'] and r.POST['phonenumber'] and r.POST['massage'] :
            contacts=Contact()
            contacts.Name=r.POST.get['Name']
            contacts.email=r.POST.get['email']
            contacts.phonenumber=r.POST.get['phonenumber']

            contacts.massage=r.POST.get['massage']
           
           
            contacts.hunter =r.user
            contacts.save()
            return redirect('home')
        else:
            return render(r ,'products/home.html',{'error':'all  fiels are required to fill'})

   return render(r,'perfectlearn/home.html')    
 
def about(r):
    return render(r,'perfectlearn/about.html')
def services(r):
    service=Service.objects
    return render(r,'perfectlearn/services.html',{'service':service})
def contacts(r):
   if r.method == 'POST':
        if r.POST['Name'] and r.POST['email'] and r.POST['phonenumber'] and r.POST['massage'] :
            contacts=Contact()
            contacts.Name=r.POST['Name']
            contacts.email=r.POST['email']
            contacts.phonenumber=r.POST['phonenumber']

            contacts.massage=r.POST['massage']
           
           
            contacts.hunter =r.user
            contacts.save()
            return redirect('home')
        else:
            return render(r ,'products/contacts.html',{'error':'all  fiels are required to fill'})

   return render(r,'perfectlearn/contacts.html')
    
def index(r):
    return render(r,'contact/index.html')
def error(r):
    return render(r,'contact/404_error.html')
def calendar(r):
    return render(r,'contact/calendar.html')
def charts(r):
    return render(r,'contact/charts.html')
def contact(r):
    c=Contact.objects
    return render(r,'contact/contact.html',{'c':c})
def dashboard(r):
    return render(r,'contact/dashboard.html')
def base1(r):
    return render(r,'contact/base1.html')    
def dashboard_2(r):
    return render(r,'contact/dashboard_2.html') 
def email(r):
    return render(r,'contact/email.html')
def general_elements(r):
    return render(r,'contact/general_elements.html')
def icons(r):
    return render(r,'contact/icons.html')    
def invoice(r):
    return render(r,'contact/invoice.html')
def login(r):
    return render(r,'contact/login.html')
def map(r):
    return render(r,'contact/map.html')
def media_gallery(r):
    return render(r,'contact/media_gallery.html')
def price(r):
    return render(r,'contact/price.html')
def profile(r):
    return render(r,'contact/profile.html')
def project(r):
    return render(r,'contact/project.html')
def settings(r):
    return render(r,'contact/settings.html')
def tables(r):
    return render(r,'contact/tables.html')
def widgets(r):
    return render(r,'contact/widgets.html')

