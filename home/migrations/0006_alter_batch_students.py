# Generated by Django 3.2.15 on 2023-03-18 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_batch_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='students',
            field=models.ManyToManyField(to='home.Student'),
        ),
    ]