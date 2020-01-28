from django.shortcuts import render, redirect

# django에서 제공하는 User 모델
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as a_login, logout as a_logout

# form 관련
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm

# Create your views here.

class Auth_join(FormView):
    template_name = 'member/auth_join.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):

        obj = User.objects.create_user(
            username=form.data.get('username'),
            password=form.data.get('password'),
            first_name=form.data.get('first_name'),
            email=form.data.get('email')
        )
        obj.save()

        return super().form_valid(form)
    
# def auth_join(request):
#     if request.method == 'GET':
#         return render(request, 'member/auth_join.html')
#     elif request.method == 'POST':
#         id = request.POST['username']
#         pw = request.POST['password']
#         na = request.POST['first_name']
#         em = request.POST['email']

#         obj = User.objects.create_user(
#             username=id,
#             password=pw,
#             first_name=na,
#             email=em
#         )
#         obj.save()

#         return redirect('/member/auth_index')

def auth_index(request):
    return render(request, 'member/auth_index.html')

# class Auth_login(FormView):
#     template_name = 'member/auth_login.html'
#     form_class = LoginForm
#     success_url = '../'
    
#     def form_valid(self, form):
        
#         obj = authenticate(username=form.data.get('username'), password=form.data.get('password'))
          
#         if obj:
#             # 세션에 추가
#             a_login(request, obj)

#         return super().form_valid(form)

def auth_login(request):
    if request.method == 'GET':
        
        form = LoginForm()

    elif request.method == 'POST':
    
        form = LoginForm(request.POST)
        if form.is_valid():
            obj = authenticate(
                username=form.data.get('username'), 
                password=form.data.get('password')
                )
            a_login(request, obj)
            return redirect('/')
            
    return render(request, 'member/auth_login.html', {'form':form})
        
# def auth_login(request):
    
#     if request.method == 'GET':
#         return render(request, 'member/auth_login.html')
#     elif request.method == 'POST':
#         id = request.POST['username']
#         pw = request.POST['password']

#         # DB에 인증
#         obj = authenticate(request, username=id, password=pw)

#         if obj:
#             # 세션에 추가
#             a_login(request, obj)
#         return redirect('/member/auth_index')

def auth_logout(request):
    if request.method == 'GET' or request.method == 'POST':
        a_logout(request)
        return redirect('/')

def auth_edit(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('/member/auth_login')
        obj = User.objects.get(username=request.user)
        return render(request, 'member/auth_edit.html', {"obj":obj})
    elif request.method == 'POST':
        id = request.POST['username']
        na = request.POST['first_name']
        em = request.POST['email']

        obj = User.objects.get(username=id)
        obj.first_name = na
        obj.email = em
        obj.save()
        return redirect('/member/auth_index')

def auth_pw(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('/member/auth_login')

        return render(request, 'member/auth_pw.html')
    elif request.method == 'POST':
        pw = request.POST['pw'] # 기존 암호
        pw1 = request.POST['pw1'] # 기존 암호
        obj = authenticate(request, username=request.user, password=pw)
        if obj:
            obj.set_password(pw1)
            obj.save()
            return redirect('/member/auth_index')
        return redirect('/member/auth_pw')

