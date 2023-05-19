from django.shortcuts import render
from django.views.generic.base import View

from .models import Post


# Алгоритм работы с контролером:
# 1 - создать модель; 2 - сделать миграцию; 3 - создать класс-контролер(View);
# 4 - создать папку для хранения шаблонов проекта и под каждое приложение создать папку с шаблонами;
# 5 - создать html-шаблон в папке с шаблонами для конкретного проекта;
# 6 - прописать в settings.py путь к шаблонам в TEMPLATES в ключе 'DIRS';
# 7 - в классе-контролере реализовать вывод render с прописанным путем к шаблону и контентом в формате словаря;
# 8 - заполнить html-шаблон контентом;
# 9 - создать в папке с приложением файл urls.py и в нем создать список urlpatterns и наполнить его по примеру, как это
# реализовано в urls.py проекта - "urlpatterns = [path('', views.SomeView.as_view())]"

class PostView(View):
    '''Контролер постов'''

    def get(self, request):
        posts = Post.objects.all()  # запрос всех записей постов
        return render(request=request, template_name='blog/blog.html', context={'post_list': posts})  # рендер объединяет шаблон, со словарем данных(которые можно получить из БД)

