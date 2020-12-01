from django.db import models

# Create your models here.
class Book(models.Model):
    bookName = models.CharField(max_length = 50, null = True)

    def __str__(self):
        return self.bookName