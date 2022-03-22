from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lybmvvsapp.urls'))  #при переходе на главную странцицу на сайте будем вызывать вот этот файл urls из папки lybmvvsapp
]
