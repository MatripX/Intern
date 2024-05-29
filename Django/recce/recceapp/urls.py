from django.urls import path
from . import views

urlpatterns =[
    path('', views.index,name="index"),
    path('home',views.home,name="homepage"),
    path('about',views.about,name="aboutpage"),
     path('services',views.services,name="servicepage"),
      path('gallery',views.gallery,name="gallerypage"),
       path('contact',views.contact,name="contactpage"),
]