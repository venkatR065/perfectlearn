from django.contrib import admin

from .models import New, Service
from .models import Course
from .models import Website

admin.site.register(Course)
admin.site.register(New)
admin.site.register(Service)
admin.site.register(Website)