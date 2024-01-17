from django.urls import path

from .views import index, about, kategory
urlpatterns = [
    path("",index, name="index"),
    path ("about/",about, name='about'),
    path ("kategory",kategory, name='kategory')
]
