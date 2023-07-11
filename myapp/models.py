from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone= models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    date = models.DateTimeField()
    def __str__(self):
        return self.name

class FaceBook(models.Model):
    user = models.CharField(max_length=122)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.user