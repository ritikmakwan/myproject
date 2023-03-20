from django.contrib import admin
from .models import Student,Batch,Trainer,JoinedStudent
# Register your models here.
admin.site.register(Student)
admin.site.register(Batch)
admin.site.register(JoinedStudent)
admin.site.register(Trainer)