from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from users.forms import LoginForm, SignupForm

# Create your views here. 함수의 이름이 같아 무한 루프
def login_view(request): 
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        print("form is_valid():", form.is_valid())
        print("form.cleaned_data:", form.cleaned_data)
        
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            
            user = auth.authenticate(request, username=username, password=password)

            if user:
                auth.login(request, user)
                return redirect("crime:landing")
            else:
                form.add_error(None,"정보가 없습니다")

        context = {"form":form}
        return render(request, "login.html", context)


    else:
        form = LoginForm()

        context = {"form": form,}
        return render(request, "login.html", context)

    #     if user is not None:
    #         auth.login(request, user)
    #         return redirect('login')
    #     else:
    #         return render(request,'login.html', {'error':'username or password is incorrect'})
    # else:
    #     return render(request,'users/login.html')

def logout_view(request):
    logout(request)

    return redirect("/users/login/")

# def logout_view(request):
#     if request.method == "POST":
#         form = LogoutForm(data=request.POST)

#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(request, username=username, password=password)

#             if user:
#                  auth.logout(request, user)
#                  return redirect("users:login")
#             else:
#                  form("로그아웃됐습니다")

#         context = {"form":form}
#         return render(request, "users/logout.html", context)
    
#     else:
#         form = LogoutForm()

#         context = {"form":form}
#         return render(request, "users/logout.html")

    #     auth.logout(request)
    #     return redirect('home')
    # return render(request,'signup.html')

def sign_up(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST, files=request.FILES)

        if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("/")
        else:
                context = {"form": form}
                return render(request,"signup.html", context)
            
    else:
        form = SignupForm()
        
    context = {"form": form}
    return render(request, "signup.html", context)

    # if request.POST['password1']==request.POST['password2']:
    #     user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
    #     auth.login(request,user)
    #     return redirect('home')
    # return render(request,'users/signup.html')