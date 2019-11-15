# Generated by Django 2.2.7 on 2019-11-15 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('initial', '0007_remove_semester_offered_courses'),
        ('institution', '0011_auto_20191114_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='degree',
            name='registration_semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='initial.Semester'),
        ),
    ]
