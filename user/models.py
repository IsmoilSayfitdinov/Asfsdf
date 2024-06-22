from django.db import models

# Create your models here.
class UserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    age = models.IntegerField()
    
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'