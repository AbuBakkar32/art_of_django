from django.db import models

# Create your models here.
class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Course(Timestamp):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=100)
    course_fee = models.CharField(max_length=100)
    course_description = models.TextField()
    course_image = models.ImageField(upload_to='course/images', default='')

    def __str__(self):
        return self.course_name

# class Student(Timestamp):
#     student_name = models.CharField(max_length=100)
#     student_email = models.CharField(max_length=100)
#     student_mobile = models.CharField(max_length=100)
#     student_address = models.TextField()
#     student_course = models.ForeignKey(Course, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.student_name
#
# class Enquiry(Timestamp):
#     enquiry_name = models.CharField(max_length=100)
#     enquiry_email = models.CharField(max_length=100)
#     enquiry_mobile = models.CharField(max_length=100)
#     enquiry_message = models.TextField()
#
#     def __str__(self):
#         return self.enquiry_name