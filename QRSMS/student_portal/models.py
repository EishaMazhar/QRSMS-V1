from django.db import models
from django.core.validators import RegexValidator, ValidationError
from django.urls import reverse
from actor.models import BATCH_YEAR_REGEX, STUDENT_YEAR_CHOICE, User
from institution.constants import UNIVERISTY_ID_REGEX
# Create your models here.

class Student(models.Model):
    @classmethod
    def create(cls, first_name,last_name,email,password, *args, **kwargs):
        print(first_name + last_name+ email+ password)
        user_created = User(first_name = first_name, last_name = last_name, password = password, email=email, is_student=True)
        user_created.save()
        last_student = Student.objects.all().order_by('arn').last()
        
        if not last_student:
            print("last student is empty")
            last_arn_number =  ((17%100)*1000000)+1
        else:
            last_arn_number = last_student.arn + 1
            
        
        student_created = cls(user=user_created,arn=last_arn_number)
        
        print("Returning created student")
        print(student_created )

        return student_created

    user = models.OneToOneField('actor.User', on_delete=models.CASCADE)
    batch = models.PositiveSmallIntegerField("batch year", validators=[BATCH_YEAR_REGEX])
    arn = models.PositiveIntegerField(
        "Admission Registration Number", name='arn')
    
    uid = models.CharField("Student ID", default="00K-0000", name="uid",
                           max_length=8, validators=[UNIVERISTY_ID_REGEX], help_text="University Student Roll Number", primary_key=True)

    degree_name_enrolled = models.CharField(max_length=255 ,null=True)
    degree_short_enrolled = models.CharField(max_length=30, null=True)
    department_name_enrolled = models.CharField(max_length=255, null=True)

    uni_mail = models.EmailField(name='uni_mail',null=True)
    current_semester = models.PositiveSmallIntegerField(name = 'current_semester', null=True, help_text ='Number of semester the student is Attending.')
    # current_semester = models.ForeignKey('initial.Semester', on_delete = models.SET_NULL, null = True)
    warning_count = models.PositiveSmallIntegerField(name='warning_count', null=True)
    attending_semester = models.BooleanField(name='attending_semester', null= True, help_text = 'If the student is currently attending classes') # If the student is currently attending classes
    student_year = models.SmallIntegerField(choices=STUDENT_YEAR_CHOICE, name='student_year', null=True)
    admission_section = models.CharField(max_length=256,null=True, blank = True)
    def __str__(self):
        return self.user.username


    class Meta:
        ordering = ('-pk',)

    def get_absolute_url(self):
        return reverse('initial_student_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('initial_student_update', args=(self.pk,))


