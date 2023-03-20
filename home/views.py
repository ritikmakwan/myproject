from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import Student,JoinedStudent,Trainer,Batch
# Create your views here.
def home(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,'succesfullt logged in')
            return render(request,'index.html')
        else:
            messages.info(request,'invalid username or password')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def addstudent(request):
    username=request.POST['email']
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    password=request.POST['password']
    user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
    user.save()
    s=Student()
    s.user=user
    s.name=fname
    s.mobile=request.POST['mobile']
    s.address=request.POST['address']
    s.edt=request.POST['e_date']
    s.remarks=request.POST['remarks']
    s.course=request.POST['course']
    s.save()
    messages.info(request,'your form is submitted')
    return render(request,'index.html')

def showstudents(request):
    st=Student.objects.all()
    return render(request,'showstudents.html',{'st':st})

def updatestudent(request):
    id=request.POST['id']
    s=Student.objects.filter(user_id=id).get()
    s.mobile=request.POST['mobile']
    s.address=request.POST['address']
    s.course=request.POST['course']
    s.remarks=request.POST['remarks']
    s.save()
    st=Student.objects.all()
    return render(request,'showstudents.html',{'st':st})

def searchstudent(request):
    if request.method=='POST':
        name=request.POST['name']
        course=request.POST['course']
        fdt=request.POST['fdt']
        tdt=request.POST['tdt']
        if name!="" and course!="" and fdt!="" and tdt!="":
            st=Student.objects.filter(name=name,course=course,edt__gte=fdt,edt__lte=tdt).all()
        elif course!="" and fdt!="" and tdt!="":
            st=Student.objects.filter(course=course,edt__gte=fdt,edt__lte=tdt).all()
        elif name!="" and fdt!="" and tdt!="":
            st=Student.objects.filter(name=name,edt__gte=fdt,edt__lte=tdt).all()
        elif name!="" and course!="":
            st=Student.objects.filter(name=name,course=course).all()
        elif name!="" and tdt!="":
            st=Student.objects.filter(name=name,edt__lte=tdt).all()
        elif name!="":
            st=Student.objects.filter(name=name).all()
        elif course!="" and fdt!="" and tdt!="":
            st=Student.objects.filter(course=course,edt__gte=fdt,edt__lte=tdt).all()
        elif course!="" and tdt!="":
            st=Student.objects.filter(course=course,edt__lte=tdt).all()
        elif course!="":
            st=Student.objects.filter(course=course).all()
        elif fdt!="" and tdt!="":
            st=Student.objects.filter(edt__gte=fdt,edt__lte=tdt).all()
        elif tdt!="":
            st=Student.objects.filter(edt__lte=tdt).all()
        return render(request,'showstudents.html',{'st':st})
        
    else:
        return render(request,'searchstudent.html') 
    
def joinstudent(request):
    if request.method=='POST':
        j=JoinedStudent()
        id=request.POST['student']
        j.student=Student.objects.filter(user_id=id).get()
        j.joined_date=request.POST['joined_date']
        j.total=request.POST['total']
        j.first_ins=request.POST['first_ins']
        j.first_date=request.POST['first_date']
        j.last_ins=request.POST['last_ins']
        j.last_date=request.POST['last_date']
        j.duration=request.POST['duration']
        j.dues=request.POST['dues']
        j.save()
        messages.info(request,'successfully updated')
        return redirect('/joinstudent')
    else:
        st=Student.objects.all()
        return render(request,'joinstudent.html',{'st':st})
    
def showjoinstudent(request):
    join=JoinedStudent.objects.all()
    return render(request,'showjoinstudent.html',{'join':join})

def updatejoinstudent(request):
    id=request.POST['id']
    j=JoinedStudent.objects.filter(id=id).get()
    j.last_ins=request.POST['last_ins']
    j.last_date=request.POST['last_date']
    j.dues=request.POST['dues']
    j.save()
    return redirect('/showjoinstudent')

def searchjoinedstudent(request):
    if request.method=='POST':
        name=request.POST['name']
        course=request.POST['course']
        fdt=request.POST['fdt']
        tdt=request.POST['tdt']
        dues=request.POST['dues']
        if name!="":
            st=Student.objects.filter(name=name).all()
            join=JoinedStudent.objects.filter(student__in=st).all()
        if course!="":
            st=Student.objects.filter(course=course).all()
            for i in st:
                join=JoinedStudent.objects.filter(student=i).all()
        if fdt!="":
            join=JoinedStudent.objects.filter(joined_date__gte=fdt).all()
        if tdt!="":
            join=JoinedStudent.objects.filter(joined_date__lte=tdt).all()
        if dues!="":
            if dues=="Remaining Dues":
                join=JoinedStudent.objects.filter(dues__gte=1)
            elif dues=="No Dues":
                join=JoinedStudent.objects.filter(dues=0)
        return render(request,'showjoinstudent.html',{'join':join})
    else:
        return render(request,'searchjoinedstudent.html')
    
def batch(request):
    if request.method=="POST":
        b=Batch()
        b.start_date=request.POST['start_date']
        id=request.POST['trainer']
        b.trainer=Trainer.objects.filter(id=id).get()
        b.bname=request.POST['bname']
        b.save()
        students=request.POST.getlist('students')
        for i in students:
            s=Student.objects.filter(user_id=i).get()
            b.students.add(s)
        return redirect('/batch')
    else:
        st=JoinedStudent.objects.all()
        t=Trainer.objects.all()
        return render(request,'batch.html',{'st':st,'t':t})
    
def trainer(request):
    if request.method=="POST":
        t=Trainer()
        t.trainer_name=request.POST['trainer_name']
        t.languages=request.POST['languages']
        t.sal=request.POST['sal']
        t.joined_date=request.POST['joined_date']
        t.time=request.POST['time']
        t.save()
        return redirect('/trainer')
    else:
        return render(request,'trainer.html')