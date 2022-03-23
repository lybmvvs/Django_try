
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),  #при переходе на главную странцицу на сайте будем вызывать вот этот файл urls из папки lybmvvsapp
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create')
]