from django.shortcuts import render

# Create your views here.

def auth_join(request):
    if request.method == 'GET':
        return render(request, 'member/auth_join.html')
    elif request.method == 'POST':
        id = request.POST['username']
        pw = request.POST['password']
        na = request.POST['first_name']
        em = request.POST['email']

        obj = User.objects.create_user(
            username=id,
            password=pw,
            first_name=na,
            email=em
        )
        obj.save()

        return redirect('/member/auth_index')

def auth_index(request):
    return render(request, 'member/auth_index.html')

def auth_login(request):
    if request.method == 'GET':
        return render(request, 'member/auth_login.html')
    elif request.method == 'POST':
        id = request.POST['username']
        pw = request.POST['password']

        # DB에 인증
        obj = authenticate(request, username=id, password=pw)

        if obj:
            # 세션에 추가
            a_login(request, obj)
        return redirect('/member/auth_index')

def auth_logout(request):
    if request.method == 'GET' or request.method == 'POST':
        a_logout(request)
        return redirect('/member/auth_index')

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

