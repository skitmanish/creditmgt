
from django.db import models
class Proview(models.Model):
                name=models.CharField(max_length=70)
                image=models.ImageField(upload_to='images/')
                number=models.IntegerField(default=0)
                email=models.EmailField(max_length=70)
                credits=models.IntegerField(default=500)

                
