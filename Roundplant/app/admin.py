from django.contrib import admin
from . models import *
# Register your models here.
class Index_display(admin.ModelAdmin):
    list_display=['name','email','phone','message']
    
    
class Contact_display(admin.ModelAdmin):
    list_display=['name','email','phone','message','subject']
class Packages_display(admin.ModelAdmin):
    list_display=['image','description']
    
class Newsevents_display(admin.ModelAdmin):
    list_display=['images','descriptions']
    
class Gallery_display(admin.ModelAdmin):
    list_display=['images']
class Subpackages_display(admin.ModelAdmin):
    list_display=['image','packagename']
   
class Subpackagesinner_display(admin.ModelAdmin):
    list_display=['Duration','Location','Price']

# class Booknow_display(admin.ModelAdmin):
#     list_display=['name','email','phone','requiment']

admin.site.register(Index,Index_display)
admin.site.register(Contact,Contact_display)
admin.site.register(Packages,Packages_display)
admin.site.register(Newsevents,Newsevents_display)
admin.site.register(Gallery,Gallery_display)
admin.site.register(Subpackages,Subpackages_display)
admin.site.register(Subpackagesinner,Subpackagesinner_display)
# admin.site.register(Booknow,Booknow_display)
