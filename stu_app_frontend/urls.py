from django.urls import path
from . import views


urlpatterns=[


path(
'',
views.landing,
name='landing'
),


path(
'login/',
views.login_view,
name='login'
),


path(
'register/',
views.register,
name='register'
),



path(
'courses/',
views.courses,
name='courses'
),


path(
'cse/',
views.cse,
name='cse'
),


path(
'ece/',
views.ece,
name='ece'
),


path(
'civil/',
views.civil,
name='civil'
),


path(
'mechanical/',
views.mechanical,
name='mechanical'
),



path(
'student-details/',
views.student_details,
name='student_details'
),
 


]