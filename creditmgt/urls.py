
from django.contrib import admin
from django.urls import path,include
from details import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('viewprofiles/',views.viewprofiles,name='viewprofiles'),
    path('contact/',views.contact,name='contact'),
    path('record/',views.record,name='record'),
    path('transfer/',views.transfer,name='transfer'),

    path('proview/',include('proview.urls')),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
