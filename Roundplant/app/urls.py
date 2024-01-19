from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('packages',views.packages,name='packages'),
    path('newsevents',views.newsevents,name='newsevents'),
    path('contactus',views.contactus,name='contactus'),
    path('gallery',views.gallery,name='gallery'),
    path('subpackages/<int:id>/',views.subpackages,name='subpackages'),
    path('subpackagesinner/<int:id>/',views.subpackagesinner,name='subpackagesinner'),
    path('subnewsevents',views.subnewsevents,name='subnewsevents'),



] +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)

