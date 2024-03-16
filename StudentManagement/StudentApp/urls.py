from django.urls import path

from StudentApp import views

urlpatterns = [
    path('',views.login_fun,name="log"),
    path('register',views.register_fun,name="reg"),
    path('home',views.home_fun,name="home"),
    path('addcourse',views.add_course_fun,name="addcourse"),
    path('displaycourse',views.display_course_fun, name="discourse"),
    path('updatecourse/<int:courseid>',views.update_course_fun,name="update_course"),
    path('delete_course/<int:courseid1>',views.delete_fun,name="delete_course"),
    path('add_student',views.add_student_fun, name="addstudent"),
    path('updatestud/<int:studid>',views.update_stud_fun, name ="update_stud"),
    path('delete_stud/<int:stid>',views.delete_stud_fun,name="delete_stud"),
    path('dispaly_stud',views.displaystud_fun,name="disstud")

]
