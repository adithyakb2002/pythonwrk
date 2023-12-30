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



admin.site.register(Index,Index_display)
admin.site.register(Contact,Contact_display)
admin.site.register(Appointment,Appointment_display)
admin.site.register(Packages,Packages_display)
