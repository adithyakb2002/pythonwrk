from django.contrib import admin
from . models import *
class Authors(admin.ModelAdmin):
    list_display=['name']


class Viewers(admin.ModelAdmin):
    list_display=['name']

# Register your models here.
admin.site.register(Author,Authors)
admin.site.register(Views,Viewers)