from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=100)
    course_fee = models.CharField(max_length=100)
    course_description = models.TextField()
    course_image = models.ImageField(upload_to='course/images', default='')

    class Meta:
        abstract = True

    def __str__(self):
        return self.course_name

class fees(Course):


