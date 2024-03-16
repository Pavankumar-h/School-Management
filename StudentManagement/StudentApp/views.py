from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from StudentApp.models import Course, Student, City


# Create your views here.

def login_fun(request):
    if request.method == "POST":
        u_user = request.POST['txtusername']
        u_password =request.POST['txtpassword']
        u2 =authenticate(username=u_user, password=u_password)
        print(u2)
        if u2 is not None:
            if u2.is_superuser:
                request.session['Uname']=u_user
                return redirect('home')
        else:
            return render(request,'login.html',{'msg':'Username and Password are not matching'})

    else:
        return render(request, 'login.html')


def register_fun(request):
    if request.method =="POST":
        user_name =request.POST['txtusername']
        user_password =request.POST['txtpassword']
        user_email= request.POST['email']
        if User.objects.filter(username=user_name).exists():
            return render(request,"register.html", {'msg':'Enter different user'})
        else:
            u1 = User.objects.create_superuser(username=user_name, password=user_password)
            u1.save()
            return redirect('log')
    else:
        return render(request, 'register.html')

def home_fun(request):
    return render(request,'home.html',{"msg": request.session['Uname']})


def add_course_fun(request):
    if request.method=="POST":
        c1 = Course()
        c1.course_name= request.POST['txtcoursename']
        c1.course_duration = request.POST['txtcourseduartion']
        c1.course_fees = int(request.POST['txtcoursefees'])
        c1.save()
        return render(request, "add_course.html", {'msg':'Course added successfully'})
    else:
        return render(request,"add_course.html")

def display_course_fun(request):
    course_details = Course.objects.all()
    return render(request, "dispaly_course.html", {'datatransfer':course_details})


def update_course_fun(request,courseid):
     c1 = Course.objects.get(id=courseid)
     if request.method == 'POST':
         c1.course_name = request.POST['txtcoursename']
         c1.course_duration =request.POST['txtcourseduartion']
         c1.course_fees = int(request.POST['txtcoursefees'])
         c1.save()
         return redirect('discourse')
     else:
        return render(request, "updatecourse.html",{'data':c1})


def delete_fun(request, courseid1):
    c2 = Course.objects.get(id=courseid1)
    c2.delete()
    return redirect('discourse')


def add_student_fun(request):
    if request.method == "POST":
        s1= Student()
        s1.Student_name = request.POST['txtstudname']
        s1.Student_ph = request.POST['phno']
        s1.student_email = request.POST['studemail']
        s1.paid_fees =int(request.POST['txtpaidfees'])
        c1 = Course.objects.get(course_fees = request.POST['txtcoursefees'])
        if s1.pending_fees > 0:
            s1.pending_fees = c1.course_fees - s1.paid_fees
        else:
            s1.pending_fees = 0
        s1.Student_course = Course.objects.get(course_name=request.POST['txtsudcourse'])
        s1.City = City.objects.get(city_name=request.POST['studcity'])
        s1.save()
        return redirect('disstud')
    else:
        course = Course.objects.all()
        city = City.objects.all()
        return render(request, "addstudent.html" ,{'course':course, 'city':city})



def displaystud_fun(request):
    stud_details =Student.objects.all()
    return render(request,"display_student.html",{'data1':stud_details})


def update_stud_fun(request,studid):
    s1 = Student.objects.get(id=studid)
    if request.method == "POST":
        s1 = Student()
        s1.Student_name = request.POST['txtstudname']
        s1.Student_ph = request.POST['phno']
        s1.student_email = request.POST['studemail']
        s1.paid_fees = int(request.POST['txtpaidfees'])
        c1 = Course.objects.get(course_fees=request.POST['txtcoursefees'])
        if s1.pending_fees > 0:
            s1.pending_fees = c1.course_fees - s1.paid_fees
        else:
            s1.pending_fees = 0
        s1.Student_course = Course.objects.get(course_name=request.POST['txtsudcourse'])
        s1.City = City.objects.get(city_name=request.POST['studcity'])
        s1.save()
        return redirect('disstud')
    else:
        course = Course.objects.all()
        city = City.objects.all()
        return render(request ,"updatestudent.html" , {'data':s1, 'citydata': city, 'coursedata':course })



def delete_stud_fun(request,stid):
    s2 = Student.objects.get(id=stid)
    s2.delete()
    return redirect('disstud')
