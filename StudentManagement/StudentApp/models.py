from django.db import models
from django.db.models import Model


# Create your models here.
class Course(models.Model):

    course_name = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=100)
    course_fees = models.BigIntegerField()

    def __str__(self):
        return  self.course_name

class City(models.Model):
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name

class Student(models.Model):
    Student_name = models.CharField(max_length=150)
    Student_ph = models.BigIntegerField()
    Student_course = models.ForeignKey(Course,on_delete=models.CASCADE)
    student_email = models.CharField(max_length=120)
    paid_fees = models.BigIntegerField()
    pending_fees = models.BigIntegerField(default=0)
    City = models.ForeignKey(City, on_delete=models.CASCADE)




