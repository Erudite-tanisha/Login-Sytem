from django.db import models

# Create your models here.
class UserDetails(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.CharField(max_length=20, unique= True)
    Password = models.CharField(max_length=12)

# Change the name of the model in admin panel
    class Meta: 
        verbose_name = 'User Detail'


