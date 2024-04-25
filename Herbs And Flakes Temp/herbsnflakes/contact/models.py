from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    mobile = models.CharField(max_length=12)
    message = models.TextField(max_length=256)
    date = models.DateField()

    def __str__(self):
        return self.name

        