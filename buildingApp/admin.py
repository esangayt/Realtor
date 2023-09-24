from django.contrib import admin

from buildingApp.models import Business, Building, Comment

# Register your models here.
admin.site.register(Business)
admin.site.register(Building)
admin.site.register(Comment)
