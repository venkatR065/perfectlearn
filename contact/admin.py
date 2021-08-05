from django.contrib import admin
from .models import Email

from .models import Contact

admin.site.register(Contact)

admin.site.register(Email)