# Generated by Django 2.2.7 on 2019-11-19 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_portal', '0004_auto_20191115_0903'),
        ('initial', '0008_semester_degree_short'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_type', models.CharField(blank=True, choices=[('F', 'Final'), ('M', 'Mid'), ('Q', 'Quiz'), ('A', 'Assignment'), ('CP', 'Class Participation'), ('L', 'Lab Marks')], max_length=256, null=True)),
                ('obtained_marks', models.PositiveIntegerField(blank=True, null=True)),
                ('total_marks', models.PositiveIntegerField(blank=True, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student_portal.Student')),
            ],
        ),
        migrations.RemoveField(
            model_name='coursesection',
            name='attendance',
        ),
        migrations.AddField(
            model_name='coursesection',
            name='average',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coursesection',
            name='maximum',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coursesection',
            name='minimum',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coursesection',
            name='standard_devition',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='MarkSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sddc', models.CharField(max_length=256, null=True)),
                ('grand_total_marks', models.PositiveIntegerField(blank=True, null=True)),
                ('Marks', models.ManyToManyField(to='initial.Marks')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student_portal.Student')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sddc', models.CharField(max_length=256, null=True)),
                ('attendance', models.ManyToManyField(to='initial.Attendance')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student_portal.Student')),
            ],
        ),
        migrations.AddField(
            model_name='coursesection',
            name='attendance_sheet',
            field=models.ManyToManyField(to='initial.AttendanceSheet'),
        ),
        migrations.AddField(
            model_name='coursesection',
            name='mark_sheet',
            field=models.ManyToManyField(to='initial.MarkSheet'),
        ),
    ]
