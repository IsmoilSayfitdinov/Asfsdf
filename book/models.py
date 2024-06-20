from django.db import models

# Create your models here.
class BooksModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    count = models.IntegerField()
    page = models.IntegerField()
    price = models.IntegerField()
    
    isbn = models.CharField(max_length=100)
    
    create_at  = models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        
    