from django.db import models

class Trecord(models.Model):
                fname=models.CharField(max_length=70)
                tname=models.CharField(max_length=70)
                amount=models.IntegerField(default=500)
                event_date=models.DateTimeField()
