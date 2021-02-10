from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('add_person', views.add_person, name='add_person'),
    path('add_article', views.add_article, name='add_article'),
    path('get_person', views.get_person, name='get_person'),
    path('get_article', views.get_article, name='get_article'),
    path('get_department', views.get_department, name='get_department'),
    path('person_list', views.person_list, name='person_list'),
    path('article_list', views.article_list, name='article_list'),
    path('department_list', views.department_list, name='department_list'),
]