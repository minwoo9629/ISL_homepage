from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
#유저에 대한 클래스를 가져옴
from django.contrib import auth
#계정에 대한 권한
from .models import Profile
from .forms import SignupForm, IDForm
from django.db import transaction
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

@transaction.atomic
def sign_up(request, id=None):

    if request.method == 'POST':
        #idcheck_form = IDForm(request.POST)
        signup_form = SignupForm(request.POST)
        #profile_form = ProfileForm(request.POST)
        if signup_form.is_valid(): #and profile_form.is_valid():
            #signup_form.get_user_id(id)
            signup_form.signup()
            #필수로 넣을수 있게 만들어야함
            signup_form.profile_save(User.objects.get(username=signup_form.cleaned_data['username']))
            return redirect('sign_in')
        else:
            #print(signup_form.errors)
            idcheck_form = IDForm()
            id = signup_form.cleaned_data['username']
            idcheck_form.initial={'username':id}
            #print(id)
            #print(signup_form.username)
            #print('un valid1')
            return render(request,'sign_up.html', {'signup_form':signup_form, 'idcheck_form':idcheck_form})
    else:
        #print(id)
        signup_form=SignupForm()
        idcheck_form = IDForm()
        
        #print(signup_form.username)
        #print('un valid2')
        signup_form.initial={'username':id}
        idcheck_form.initial={'username':id}
        #profile_form = ProfileForm()
    
    return render(request,'sign_up.html', {'signup_form':signup_form, 'idcheck_form':idcheck_form, 'check':id}) #'profile_form':profile_form}) 
    # 실패하는경우 sign_up.html에 머문다.

def id_check(request):
    if request.method == 'POST':
        signup_form=SignupForm()
        idcheck_form = IDForm(request.POST)
        if idcheck_form.is_valid():
            clean_id = idcheck_form.clean_username()
            print('valid')
            #print(clean_id)
            return redirect('sign_up', id=clean_id)
        else:
            print('fail')
            return render(request,'sign_up.html', {'signup_form':signup_form, 'idcheck_form':idcheck_form})
            
    else:
        print('error')
        
        
        return redirect('sign_up')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        # 사용자가 입력한 ID를 username에 담는다.
        password = request.POST['password']
        # 사용자가 입력한 password를 passwor에 담는다.
        user = auth.authenticate(request, username=username, password=password)
        # 데이터베이스에 입력한 username과 password가 있는지 확인한다.
        if user is not None:
            auth.login(request, user)
            #ID와 password가 존재하면 로그인
            # messages.info(request,'로그인 되었습니다.')
            # 로그인 성공시 성공 알림 띄우기
            return redirect("home")
        else:
            return render(request, 'sign_in.html', {'error': 'ID or password is incorrect.'})
    else:
        return render(request, 'sign_in.html')
    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request,"sign_in.html")
