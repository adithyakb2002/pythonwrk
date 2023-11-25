from django.contrib import admin
from . models import *

class Department_dis(admin.ModelAdmin):
    list_display=['name']


class Batch_dis(admin.ModelAdmin):
    list_display=['batch']     

class Teacher_dis(admin.ModelAdmin):
    list_display=['name','dept']    
class Student_dis(admin.ModelAdmin):
    list_display=['name','batch','teacher']    

# Register your models here.
admin.site.register(Department,Department_dis)
admin.site.register(Batch,Batch_dis)
admin.site.register(Teacher,Teacher_dis)
admin.site.register(Student,Student_dis)