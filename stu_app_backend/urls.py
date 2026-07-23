from django.urls import path
from . import views



urlpatterns=[


path(
    'register/',
    views.register,
    name='register'
),


path(
    'login/',
    views.login_view,
    name='login'
),


path(
    'logout/',
    views.logout_view,
    name='logout'
),


]





from django.urls import path
from . import views



urlpatterns=[


path(
'add/',
views.add_student,
name='add_student'
),



path(
'students/',
views.student_list,
name='student_list'
),



path(
'update/<int:id>/',
views.update_student,
name='update_student'
),



path(
'delete/<int:id>/',
views.delete_student,
name='delete_student'
),


]