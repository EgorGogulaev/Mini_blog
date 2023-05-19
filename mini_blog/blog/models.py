from django.db import models

class Post(models.Model):
    '''Таблица постов в блоге'''

    title = models.CharField('Заголовок поста', max_length=150)
    description = models.TextField('Текст поста')
    author = models.CharField('Автор', max_length=100)
    date_publication = models.DateField('Дата публикации')

    def __str__(self):
        return f"{self.author}, {self.title}"

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

