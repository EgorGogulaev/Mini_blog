# (по сути - набор маршрутов) Этот файл создается для того, чтобы приложение было более обособленным и содержало в себе свои url-адреса для доступа.(это не обязятельно делать, но более правильно).
from django.urls import path
from . import views  # '.' - это ссылка на корневой файл

urlpatterns = [path('', views.PostView.as_view())]  # Связываем представление с URL - адресом
