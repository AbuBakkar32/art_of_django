from django.db import models


# Create your models here.

class Timestamp(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Student(Timestamp):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Fees(Timestamp):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name
