from django.urls import path

from .views import index, about, otzyvy
urlpatterns = [
    path("",index, name="index"),
    path ("about/",about, name='about'),
    path ("otzyvy/",otzyvy, name='otzyvy'),
]
