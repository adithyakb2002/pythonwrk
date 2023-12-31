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

class Ayushsilverplan_display(admin.ModelAdmin):
    list_display=['image','t1','t2','t3','t4','t5','name','cost']

class Branches_display(admin.ModelAdmin):
    list_display=['images','descriptions']

class Subblog_display(admin.ModelAdmin):
    list_display=['image','heading1','heading2','heading3','paragraph2','paragraph3']


admin.site.register(Index,Index_display)
admin.site.register(Contact,Contact_display)
admin.site.register(Appointment,Appointment_display)
admin.site.register(Packages,Packages_display)
admin.site.register(Blog,Blog_display)
admin.site.register(Branches,Branches_display)
admin.site.register(Gallery,Gallery_display)
admin.site.register(Ayushsilverplan,Ayushsilverplan_display)
admin.site.register(Sub_blog,Subblog_display)
