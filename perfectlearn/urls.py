
from django.contrib import admin
from django.urls import path,include
from contact import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', views.base,name='base'),
    path('', views.home,name='home'),
    path('', views.cont,name='home'),
    
    path('contacts/', views.contacts,name='contacts'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('contact/',include('contact.urls')),
    
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

