# Generated by Django 3.2.15 on 2023-03-14 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='joinedstudent',
            name='dues',
            field=models.IntegerField(default=0),
        ),
    ]
