from django.db import models

# Create your models here.
class test_tbl(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField()
    tem  = models.IntegerField()
    Delete = models.BooleanField(default=False)
    def __str__(self):
        return (self.name)
class test1_tbl(models.Model):
    sname = models.CharField(max_length=20)
    sdate = models.DateTimeField()
    stem  = models.IntegerField()
    sdelete = models.BooleanField(default=False)
    #¹ØÁªtest_tbl
    stest = models.ForeignKey("test_tbl",on_delete=models.CASCADE)
    def __str__(self):
        return (self.sname)

class picture(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField()
    image_path =models.CharField(max_length=100)
    def __str__(self):
        return (self.name)