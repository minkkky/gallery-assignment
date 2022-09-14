from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import ApplyLog, User as UserModel
from .models import UserInfo as UserInfoModel
from .models import ApplyLog as ApplyLogModel
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required


class SignUpView(View):
    def get(self, request):
        return render(request, 'user/sign-up.html')

    def post(self, request):
        username = request.POST.get('id', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        if password != password2:
            return render(request, 'user/sign-up.html', {'error': '패스워드를 확인해주세요!'})
        else:
            if username == '' or password == '':
                return render(request, 'user/sign-up.html', {'error': '입력되지 않은 정보가 있습니다!'})

            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/sign-up.html', {'error':'사용자가 존재합니다.'})
            else:
                UserModel.objects.create_user(username=username, password=password)
                return redirect('/sign-in')


class SignInView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return redirect('/arts')
        else:
            return render(request, 'user/sign-in.html')

    def post(self, request):
        username = request.POST.get('id', '')
        password = request.POST.get('password', '')
        me = auth.authenticate(request, username=username, password=password)
        if me:
            auth.login(request, me)
            return redirect("/arts")
        else:
            return render(request,'user/sign-in.html',{'error':'ID 혹은 패스워드를 확인 해 주세요'})


class ApplyLogView(View):
    def get(self, request):
        return render(request, 'user/apply.html')

    def post(self, request):
        user = request.user
        name = request.POST.get('name', '')
        gender = request.POST.get('gender', '')
        birth = request.POST.get('birth', '')
        email = request.POST.get('email', '')
        # phone = request.POST.get('phone', '')
        phone1 = request.POST.get('phone1', '')
        phone2 = request.POST.get('phone2', '')
        phone3 = request.POST.get('phone3', '')
        phone = f'{phone1}-{phone2}-{phone3}'

        UserInfoModel.objects.create(
            user=user,
            name=name,
            gender=gender,
            birth=birth,
            email=email,
            phone=phone
        )

        return redirect("/arts")


@login_required
def logout(request):
    auth.logout(request)
    return redirect("/arts")