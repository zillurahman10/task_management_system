from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'homepage'),
    path('task/', include('task.urls')),
    path('show_task/', include('show_task.urls')),
    path('category/', include('category.urls'))
]
