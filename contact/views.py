from contact.models import Banner, Contact
from django.shortcuts import render
from django.shortcuts import redirect
from contact.models import Email
from courses.models import Service, Website
from courses.models import Course
from courses.models import New
from .forms import CourseForm
from .forms import NewForm

def base(r):
    if r.method == 'POST':
        if r.POST['email'] :
            emails=Email()
            emails.email=r.POST.get('email')
            
            emails.save()
            return redirect('home')
        else:
            return render(r ,'perfectlearn/base.html',{'error':'all  fiels are required to fill'})

    return render(r ,'perfectlearn/base.html')
    
  



def home(r):
    courses=Course.objects
    news=New.objects
    banner =Banner.objects
    
    
    return render(r,'perfectlearn/home.html',{'courses':courses,'news':news,'banner':banner})
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
    courses=Course.objects
    return render(r,'perfectlearn/about.html',{'courses':courses})
def services(r):
    service=Service.objects
    website=Website.objects
    return render(r,'perfectlearn/services.html',{'service':service,'website':website})
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
def emails(r):
    c=Email.objects
    return render(r,'contact/emails.html',{'c':c})
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
def service(r):
    service=Service.objects
    return render(r,'contact/service.html',{'service':service})
def website(r):
    c=Website.objects
    return render(r,'contact/website.html',{'c':c})
def news(r):
    news=New.objects
    return render(r,'contact/news.html',{'news':news})    
def courses(r):
    courses=Course.objects
    return render(r,'contact/course.html',{'courses':courses})       
def banner(r):
    banner =Banner.objects
    
    
    return render(r,'perfectlearn/home.html',{'banner':banner})
def edit(r,pk):
    courses=Course.objects.get(id=pk) 

    form=CourseForm(instance=courses)
    if r.method =='POST':  
        form=CourseForm(r.POST,r.FILES,instance=courses)
        if form.is_valid():
            form.save()
            return redirect('courses')
            
    context={
        "form":form
    }
    return render(r,'contact/edit.html',context)  
def addcourses(r):
    form =CourseForm()
    if r.method=="POST":
        form =CourseForm(r.POST,r.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses')    

    else:
        form =CourseForm()
    context={
        "form":form



     }   
    return render(r,'contact/addcourses.html',context)         
def deletecourse(r,pk):
    course=Course.objects.get(id=pk)
    course.delete()
    return redirect('courses')     
def addnews(r):
    form =NewForm()
    if r.method=="POST":
        form =NewForm(r.POST,r.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')    

    else:
        form =NewForm()
    context={
        "form":form



     }   
    return render(r,'contact/addnews.html',context)   
def updatenews(r,pk):
    news=New.objects.get(id=pk) 

    form=NewForm(instance=news)
    if r.method =='POST':  
        form=NewForm(r.POST,r.FILES,instance=news)
        if form.is_valid():
            form.save()
            return redirect('news')
            
    context={
        "form":form
    }
    return render(r,'contact/updatenews.html',context)      
def deletenews(r,pk):
    news=New.objects.get(id=pk)
    news.delete()
    return redirect('news')     