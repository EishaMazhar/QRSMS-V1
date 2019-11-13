from django.db import models
from django.core.validators import RegexValidator, ValidationError
from django.urls import reverse
from actor.models import User
# Create your models here.


class Faculty(models.Model):
    user = models.OneToOneField('actor.User', on_delete=models.CASCADE)

    @classmethod
    def create(cls,user = None, **kwargs):
        if user is None:
            username = None
            password = None
            if 'username' in kwargs['username']:
                username = kwargs['username']
            if 'password' in kwargs['password']:
                password = kwargs['password']

            u = User.create(username = username, password = password, is_faculty = True, is_employee = True)
            user = u

        t = cls(user = user)
        t.save()
        return t

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = "Faculty Supervisors"

    def get_absolute_url(self):
        return reverse('initial_faculty_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('initial_faculty_update', args=(self.pk,))