from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('add_person', views.add_person, name='add_person'),
]