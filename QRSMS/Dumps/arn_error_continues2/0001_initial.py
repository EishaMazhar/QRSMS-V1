# Generated by Django 2.2.5 on 2019-09-13 20:13

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('U', 'UNDEFINED'), ('O', 'OTHER')], max_length=50, verbose_name='Gender')),
                ('is_teacher', models.BooleanField(default=False, help_text='True if the User is a Teacher.')),
                ('is_student', models.BooleanField(default=False, help_text='True if the User is a Student.')),
                ('is_faculty', models.BooleanField(default=False, help_text='True if the User is a Faculty Member.')),
                ('is_maintainer', models.BooleanField(default=False, help_text='True if the User is a Mainatiner or Project Developer.')),
                ('CNIC', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('[0-9]{5}-[0-9]{7}-[0-9]{1}', message='Invalid CNIC')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_name', models.CharField(max_length=50)),
                ('course_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('course_short', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_level', models.CharField(max_length=255, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('uni_id', models.AutoField(primary_key=True, serialize=False, verbose_name='University Registration ID')),
                ('name', models.CharField(default='FAST NUCES', help_text='Name of Univeristy', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=10)),
                ('nu_email', models.CharField(max_length=100)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ARN', models.PositiveIntegerField(null=True, verbose_name='Admission Registration Number')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_season', models.SmallIntegerField(choices=[(1, 'FALL'), (2, 'SPRING'), (3, 'SUMMER')])),
                ('Semester Year', models.DateField()),
                ('Semester Start Date', models.DateField()),
                ('Semester End Date', models.DateField()),
                ('offered_courses', models.ManyToManyField(related_name='semester_offered', to='initial.Course')),
                ('students_registered', models.ManyToManyField(related_name='students_registered', to='initial.Student')),
                ('teachers_available', models.ManyToManyField(related_name='teachers_available', to='initial.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Faculty Supervisors',
            },
        ),
        migrations.CreateModel(
            name='Campuses',
            fields=[
                ('campus_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Campus ID')),
                ('Address', models.CharField(help_text='Address of Campus', max_length=255)),
                ('campus_name', models.CharField(help_text='Name of Campus of University', max_length=255)),
                ('campus_city', models.CharField(help_text='City Name of Campus', max_length=255)),
                ('name', models.ForeignKey(default='0', help_text='A university can have many campuses', on_delete=django.db.models.deletion.SET_DEFAULT, to='initial.University', verbose_name='Universities Campus')),
            ],
        ),
    ]
