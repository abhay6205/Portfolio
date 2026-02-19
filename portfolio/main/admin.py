from django.contrib import admin

# Register your models here.
from .models import Project, Experience, ContactMessage, Blog

admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(ContactMessage)
admin.site.register(Blog)