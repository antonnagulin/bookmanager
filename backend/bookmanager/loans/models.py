from django.db import models
from django.core.exceptions import ValidationError
from books.models import Book
from readers.models import Reader
from datetime import date, timedelta


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name="Читатель")
    loan_date = models.DateField("Дата выдачи", auto_now_add=True, blank=True)
    due_date = models.DateField("Срок возврата", blank=True)
    return_date = models.DateField("Дата возврата", blank=True, null=True)

    def clean(self):
        super().clean()

        if self.book.available_copies <= 0 and not self.pk:
            raise ValidationError(f"Нет доступных экземпляров книги '{self.book.title}'.")

    def save(self, *args, **kwargs):
        # Устанавливаем срок возврата при создании
        if not self.due_date:
            self.due_date = self.loan_date + timedelta(days=14)

        # Проверяем доступность перед сохранением
        self.clean()

        # Сохраняем старое состояние, если это обновление
        if self.pk:
            old_loan = Loan.objects.get(pk=self.pk)
            book_changed = old_loan.book != self.book
            was_returned = old_loan.return_date and not self.return_date
            not_returned_anymore = not old_loan.return_date and self.return_date

            super().save(*args, **kwargs)

            # Если поменяли книгу — корректируем обе
            if book_changed:
                old_loan.book.available_copies += 1
                old_loan.book.save()
                self.book.available_copies -= 1
                self.book.save()
            # Если вернули — увеличиваем доступные копии
            elif not_returned_anymore:
                self.book.available_copies += 1
                self.book.save()
            # Если отменили возврат — уменьшаем
            elif was_returned:
                self.book.available_copies -= 1
                self.book.save()
        else:
            # Новая выдача
            super().save(*args, **kwargs)
            self.book.available_copies -= 1
            self.book.save()

    def __str__(self):
        return f"{self.book} — {self.reader}"

    class Meta:
        verbose_name = "Выдача"
        verbose_name_plural = "Выдачи"
