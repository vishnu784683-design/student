from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

from .models import Student




# Register

def register(request):

    if request.method=="POST":


        username=request.POST['username']

        email=request.POST['email']

        password=request.POST['password']

        phone=request.POST['phone']

        branch=request.POST['branch']

        year=request.POST['year']



        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists"
            )

            return redirect('register')



        user=User.objects.create_user(
            

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



    return render(
        request,
        "register.html"
    )





# Login

def login_view(request):


    if request.method=="POST":


        username=request.POST['username']

        password=request.POST['password']



        user=authenticate(

            username=username,

            password=password

        )



        if user is not None:


            login(
                request,
                user
            )


            return redirect(
                'courses'
            )



        else:


            messages.error(

                request,

                "Invalid Username or Password"

            )



    return render(
        request,
        "login.html"
    )





# Logout

def logout_view(request):

    logout(request)

    return redirect('login')






















from django.shortcuts import render,redirect
from .models import Student



def add_student(request):

    if request.method=="POST":

        name=request.POST['name']

        email=request.POST['email']

        phone=request.POST['phone']

        branch=request.POST['branch']

        year=request.POST['year']


        Student.objects.create(

            name=name,

            email=email,

            phone=phone,

            branch=branch,

            year=year

        )


        return redirect('student_list')


    return render(request,'add_student.html')
def student_list(request):

    students=Student.objects.all()


    return render(
        request,
        'student_list.html',
        {
            'students':students
        }
    )
    
def update_student(request,id):

    student=Student.objects.get(id=id)


    if request.method=="POST":

        student.name=request.POST['name']

        student.email=request.POST['email']

        student.phone=request.POST['phone']

        student.branch=request.POST['branch']

        student.year=request.POST['year']


        student.save()


        return redirect('student_list')


    return render(
        request,
        'update_student.html',
        {
            'student':student
        }
    )
def delete_student(request,id):

    student=Student.objects.get(id=id)


    student.delete()


    return redirect('student_list')