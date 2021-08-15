from django.contrib import admin
from .models import Email
from .models import Banner

from .models import Contact

admin.site.register(Contact)

admin.site.register(Email)
admin.site.register(Banner)