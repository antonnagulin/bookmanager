from django.db import models

class Book(models.Model):
    title = models.CharField("Название", max_length=200)
    author = models.CharField("Автор", max_length=100)
    isbn = models.CharField("ISBN", max_length=13, unique=True, blank=True, null=True)
    total_copies = models.PositiveIntegerField("Всего экземпляров", default=1)
    available_copies = models.PositiveIntegerField("Доступно экземпляров", default=0)

    def save(self, *args, **kwargs):
        # При сохранении устанавливаем available_copies, если не задано
        if self.available_copies == 0:
            self.available_copies = self.total_copies
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
