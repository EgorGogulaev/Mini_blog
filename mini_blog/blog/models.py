from django.db import models

class Post(models.Model):
    '''Таблица постов в блоге'''

    title = models.CharField('Заголовок поста', max_length=150)
    description = models.TextField('Текст поста')
    author = models.CharField('Автор', max_length=100)
    date_publication = models.DateField('Дата публикации')
    # для работы с изображениями необходимо скачать библиотеку - pillow
    img = models.ImageField('Изображение', upload_to='image/%Y')  # upload_to - атрибут, определяющий, где будут сохраняться изображения (%Y означает, что будет дополнительная вложенность, где вложенные папки будут именоваться текущем годом в период загрузки информации)


    def __str__(self):
        return f"{self.author}, {self.title}"

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

