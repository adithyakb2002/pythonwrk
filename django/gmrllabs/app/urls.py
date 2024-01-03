from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
       path('aboutus',views.aboutus,name='aboutus'),
       path('packages',views.packages,name='packages'),
       path('department',views.department,name='department'),
       path('blog',views.blog,name='blog'),
       path('gallery',views.gallery,name='gallery'),
       path('branches',views.branches,name='branches'),
       path('contactus',views.contactus,name='contactus'),
       path('bookanappointment',views.bookanappointment,name='bookanappointment'),
       path('test',views.test,name='test'),
       path('ayushsilverplan/<int:id>/',views.ayushsilverplan,name='ayushsilverplan'),
       path('subblog',views.subblog,name='subblog'),

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
