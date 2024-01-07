from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    about_course=models.CharField(max_length=1000)
    course_overview=models.CharField(max_length=500)
    course_topic=models.CharField(max_length=500)
    
    def __str__(self):
         return self.course_name

    
class Enquiry(models.Model):
    enquiry_name=models.CharField(max_length=100)
    Email=models.CharField( max_length=50)
    phone=models.CharField(max_length=50)
    message=models.CharField(max_length=200)
    
    def __str__(self):
        return self.Email
    
class Placement(models.Model):
    name=models.CharField(max_length=100)
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    
class Carrers(models.Model):
    position=models.CharField(max_length=100)
    
    
class Carrerapply(models.Model):
    your_name=models.CharField(max_length=100)
    Email=models.ForeignKey(Course,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    document=models.FileField(upload_to='document/')
    
class Success(models.Model):
    about=models.CharField(max_length=500)
    a_name=models.CharField(max_length=100)