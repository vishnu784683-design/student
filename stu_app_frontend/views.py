from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

from stu_app_backend.models import Student



def landing(request):

    return render(request,'landing.html')



# REGISTER

def register(request):

    if request.method=="POST":


        name=request.POST['first_name']

        email=request.POST['email']

        username=request.POST['username']

        password=request.POST['password']

        confirm=request.POST['confirm_password']

        phone=request.POST['phone']

        branch=request.POST['branch']

        year=request.POST['year']


        if password != confirm:

            messages.error(
                request,
                "Password not matching"
            )

            return redirect('register')



        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists"
            )

            return redirect('register')



        user=User.objects.create_user(

            first_name=name,

            username=username,

            email=email,

            password=password

        )



        Student.objects.create(

            user=user,

            phone=phone,

            branch=branch,

            year=year

        )


        messages.success(
            request,
            "Registration Successful"
        )


        return redirect('login')



    return render(request,'register.html')




# LOGIN

def login_view(request):

    if request.method=="POST":


        username=request.POST['username']

        password=request.POST['password']



        user=authenticate(

            username=username,

            password=password

        )


        if user is not None:


            login(request,user)


            return redirect('dashboard')



        else:


            messages.error(

                request,

                "Invalid Username or Password"

            )



    return render(request,'login.html')






# DASHBOARD

def dashboard(request):

    return render(
        request,
        'dashboard.html'
    )





# COURSES

def courses(request):

    return render(
        request,
        'courses.html'
    )





def cse(request):

    return render(
        request,
        'cse.html'
    )



def ece(request):

    return render(
        request,
        'ece.html'
    )



def civil(request):

    return render(
        request,
        'civil.html'
    )



def mechanical(request):

    return render(
        request,
        'mechanical.html'
    )






# STUDENT DETAILS


def student_details(request):

    students=Student.objects.all()


    return render(

        request,

        "student_details.html",

        {
            "students":students
        }

    )