from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('add_person', views.add_person, name='add_person'),
    path('add_article', views.add_article, name='add_article'),
    path('get_person', views.get_person, name='get_person'),
    path('get_article', views.get_article, name='get_article'),
    path('get_department', views.get_department, name='get_department'),
]