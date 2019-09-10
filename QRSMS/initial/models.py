from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_admin =  models.BooleanField(default=False)
    CNIC = models.CharField(max_length=15, validators=[RegexValidator("[0-9]{5}-[0-9]{7}-[0-9]{1}", message="Invalid CNIC")], name="CNIC")

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50,name="course_name")
    course_code = models.CharField(max_length=20,primary_key = True, name="course_code")
    course_short = models.CharField(max_length=50)
    def __str__(self):
        return self.course_name
        

# class Student(models.Model):
#     student_id = models.CharField(max_length=8,primary_key=True, validators = [RegexValidator("^[A-Z][0-9]{2}-[0-9]{4}$", message = "Invalid Student ID")], name="student_id_n")

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, default = None)
    department = models.CharField(max_length=10)
    nu_email = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    class Meta:
        verbose_name_plural = "Faculty Supervisors"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Semester(models.Model):
    offered_courses = models.ManyToManyField(Course,related_name = "semester_offered")
    SEMSESTER_CHOICES = (
        (1,"FALL"),
        (2,"SPRING"),
        (3, "SUMMER")
    )
    semester_time = models.SmallIntegerField(choices=SEMSESTER_CHOICES, name="semester_season")
    semester_year = models.DateField(name="Semester Year")
    start_date = models.DateField(name="Semester Start Date")
    end_date = models.DateField(name="Semester End Date")
    teachers_available = models.ManyToManyField(Teacher, related_name="teachers_available")
    students_registered = models.ManyToManyField(Student, related_name="students_registered")
