from django.contrib import admin
from django.urls import path
from .views import prueba_pagina

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',prueba_pagina)
]
