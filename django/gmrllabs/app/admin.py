from django.contrib import admin
from . models import *
# Register your models here.
class Index_display(admin.ModelAdmin):
    list_display=['name','email','phone','message']

class Contact_display(admin.ModelAdmin):
    list_display=['name','email','phone','message','subject']

class Appointment_display(admin.ModelAdmin):
    list_display=['name','email','phone','message','date','time','address','gender','age']

class Packages_display(admin.ModelAdmin):
    list_display=['image','description']

class Blog_display(admin.ModelAdmin):
    list_display=['image','description']

class Branches_display(admin.ModelAdmin):
    list_display=['images','descriptions']
class Gallery_display(admin.ModelAdmin):
    list_display=['images']


admin.site.register(Index,Index_display)
admin.site.register(Contact,Contact_display)
admin.site.register(Appointment,Appointment_display)
admin.site.register(Packages,Packages_display)
admin.site.register(Blog,Blog_display)
admin.site.register(Branches,Branches_display)
admin.site.register(Gallery,Gallery_display)
