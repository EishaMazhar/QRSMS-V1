# Generated by Django 2.2.5 on 2019-09-16 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='uni_name',
            field=models.ForeignKey(help_text='A university can have many campuses', on_delete=django.db.models.deletion.CASCADE, to='institution.University', verbose_name='Universities Campus'),
        ),
    ]
