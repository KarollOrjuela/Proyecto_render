from django.db import models

# Create your models here.
# Modelo principal donde se guardarán los datos ingresados
class Project(models.Model):
    Title = models.CharField(max_length= 50)
    Description = models.TextField()
    Created_at = models.DateTimeField(auto_now=True)
    
