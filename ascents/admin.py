from django.contrib import admin

from .models import Ascent, Grade

# adding the mentioned models to the admin page to edit them there
admin.site.register(Ascent)
admin.site.register(Grade)