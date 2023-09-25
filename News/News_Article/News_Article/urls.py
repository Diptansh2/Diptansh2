"""
URL configuration for AnandNirnaya project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Anand import views
from django.conf import settings
from django.conf.urls.static import static
from Anand.views import news1
from schedule.views import CalendarView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('navbar/',views.news1, name='news1'),
    path('base/',views.news),
    path('top5/', views.latest, name='latest'),
    path('sport/',views.sport, name='sport'),
    path('international/',views.international),
    path('tech/',views.technical),
    path('login/', views.loginview),
    path('register/', views.registerview),
    path('dashboard/',views.dashboardview),
    path('astrology/', views.astrology),
    path('lifestyle/', views.lifestyle),
    path('logout/',views.logout),
    path('top5post/', views.latestpost, name='latestpost'),
    path('sportpost/',views.sportpost, name='sportpost'),
    path('internationalpost/',views.internationalpost, name='internationalpost'),
    path('techpost/',views.technicalpost, name='technicalpost'),
    path('astrologypost/',views.astrologypost, name='astrologypost'),
    path('lifestylepost/',views.lifestylepost, name='lifestylepost'),
    path('leftadd/', views.leftpost, name='leftpost'),
    path('rightadd/', views.rightpost, name='rightpost'),
    path('left/', views.left),
    path('right/', views.right),
    # path('pdf/', views.upload_pdf, name='upload_pdf'),
    # path('pdf_detail/<int:pk>/', views.pdf_detail, name='pdf_detail'),
    # path('success/',views.welcome),
path('calendar/', views.calendar_view, name='calendar'),
     #path('calendar/<slug:calendar_slug>/', CalendarView.as_view(), name='calendar'),
    # Other URL patterns for your app
    
       
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






