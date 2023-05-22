"""
URL configuration for mini_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # include - позволяет подключить URL - адреса из других приложений
from django.conf import settings  # Нужно для реализации проверки "if settings.DEBUG: ..."
from django.conf.urls.static import static  # -=-

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),

]
if settings.DEBUG:  # Если режим отладки, то добавляем статику в url-паттерны
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
