from django.db import models
from django.contrib.auth.models import User
import datetime
class Student(models.Model):
    user=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=11)
    address=models.CharField(max_length=50)
    course=models.CharField(max_length=20)
    edt=models.DateField(auto_now=False)
    remarks=models.CharField(max_length=100)
    name=models.CharField(max_length=20,default=None)
    def __str__(self) -> str:
        return self.user.username
    
    
class JoinedStudent(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    joined_date=models.DateField(auto_now=False)
    total=models.IntegerField()
    first_ins=models.IntegerField()
    first_date=models.DateField(auto_now=False)
    last_ins=models.IntegerField()
    last_date=models.DateField(auto_now=False)
    duration=models.CharField(max_length=20)
    dues=models.IntegerField(default=0)
    def __str__(self) -> str:
        return str(self.last_date.strftime("%Y-%m-%d"))
class Trainer(models.Model):
    trainer_name=models.CharField(max_length=20)
    languages=models.CharField(max_length=30)
    sal=models.IntegerField()
    joined_date=models.DateField(auto_now=False)
    time=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.trainer_name    
class Batch(models.Model):
    students=models.ManyToManyField(Student)
    start_date=models.DateField(auto_now=False)
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    bname=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.bname
    

    
