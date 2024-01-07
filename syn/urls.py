from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('blog/',views.blog,name='blog'),
    path('softwareblog/',views.softwareblog,name='softwareblog'),
    path('cloudblog/',views.cloudblog,name='cloudblog'),
    path('digitalmarketing/',views.digitalmarketing,name='digitalmarketing'), 
    path('carrers/',views.carrers,name='carrers'),
    path('webdesigner/',views.webdesigner,name='webdesigner'),
    path('seniordeveloper/',views.seniordeveloper,name='seniordeveloper'),
    path('courses/',views.courses,name='courses'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('placements/',views.placements,name='placements'),
    path('contactus/',views.contactus,name='contactus'),
    path('success/',views.success,name='success'),
    path('coursedigital/',views.coursedigital,name='coursedigital'),
    path('vmsphere/',views.vmsphere,name='vmsphere'),
    path('ciso/',views.ciso,name='ciso'),
    path('az/',views.az,name='az'),
    path('wsa/',views.wsa,name='wsa'),
    path('redhat/',views.redhat,name='redhat'),
    path('compa/',views.compa,name='compa'),
    path('phpfullstack/',views.phpfullstack,name='phpfullstack'),
    path('pythonfullstack/',views.pythonfullstack,name='pythonfullstack'),
    path('compnet/',views.compnet,name='compnet'),
    path('aws/',views.aws,name='aws'),
]