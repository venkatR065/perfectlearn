

from django.urls import path
from . import views

urlpatterns = [
  
    path('index', views.index,name='index'),
    path('error', views.error,name='error'),
    path('calendar', views.calendar,name='calendar'),
    path('charts', views.charts,name='charts'),
    path('contact', views.contact,name='contact'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('base1', views.base1,name='base1'),
    path('dashboard_2', views.dashboard_2,name='dashboard_2'),
    path('email', views.email,name='email'),
    path('general_elements', views.general_elements,name='general_elements'),
    path('icons', views.icons,name='icons'),
    path('invoice', views.invoice,name='invoice'),
    path('map', views.map,name='map'),
    path('login', views.login,name='login'),
    path('media_gallery', views.media_gallery,name='media_gallery'),
    path('price', views.price,name='price'),
    path('profile', views.profile,name='profile'),
    path('project', views.project,name='project'),
    path('settings', views.settings,name='settings'),
    path('tables', views.tables,name='tables'),
    path('widgets', views.widgets,name='widgets'),
    

    
  
   
   

] 

