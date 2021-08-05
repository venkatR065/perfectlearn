from django.contrib import admin

from .models import New, Service
from .models import Course

admin.site.register(Course)
admin.site.register(New)
admin.site.register(Service)