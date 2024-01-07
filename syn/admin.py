from django.contrib import admin
from .models import *

# Register your models here.
class Course_display(admin.ModelAdmin):
    list_display=['course_name','image','about_course','course_overview','course_topic']
    
  
class Placement_display(admin.ModelAdmin):
    list_display=['course_name','name']
    
    
class Success_display(admin.ModelAdmin):
    list_display=['about','a_name']    
       
class Enquiry_display(admin.ModelAdmin):
    list_display=['enquiry_name','Email','phone','message']
    
admin.site.register(Course,Course_display)
admin.site.register(Placement,Placement_display)
admin.site.register(Success,Success_display)
admin.site.register(Enquiry,Enquiry_display)
