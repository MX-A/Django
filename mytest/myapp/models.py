from django.db import models

# Create your models here.

class s821(models.Model):
    name = models.CharField(max_length=30)
    UA = models.FloatField()
    UB = models.FloatField()
    UC = models.FloatField()
    IA = models.FloatField()
    IB = models.FloatField()
    IC = models.FloatField()
    date = models.DateTimeField()
    def __str__(self):
        return (self.name)