from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.http import is_safe_url
from django.views import View
import hashlib
from django.contrib.auth.hashers import make_password

from .models import User
REDIRECT_FIELD_NAME = 'next'
# Create your views here.
class UserLogin(View):
    model = User
    fields = ['username', 'password']
    template_name = 'user/login.html'

    def form_valid(self, form):
        obj = form.instance
        obj.user = self.request.user
        return super(UserLogin, self).form_valid(form)


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    if request.method == "GET":
        return render(request,"user/register.html")
    if request.method == "POST":
        nick = request.POST.get("nick",'').lower().strip()
        password = request.POST.get("password", '')
        if nick == "" or password == "":
            data = {"nick":nick, "msg": '请输入用户名或密码'}
            return render(request,"user/register.html", data)
        if User.objects.filter(nick=nick).exists():
            data = {"nick":nick, "msg": '该昵称已存在'}
            return render(request,"user/register.html", data)
        password = make_password(password)
        user = User(nick=nick, password=password)
        user.save()
        return HttpResponseRedirect(reverse('index'))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('index'))
        nick = request.GET.get("nick", "")

        next_page = request.GET.get(REDIRECT_FIELD_NAME, "")  # 默认 next
        if next_page == "":
            next_page = reverse("index")
        if not is_safe_url(url=next_page, host=request.get_host()):
            next_page = reverse("index")
        request.session['next_page'] = next_page
        return render(request, "user/login.html", {"nick": nick})
    elif request.method == "POST":
        nick = request.POST.get("nick",'').lower().strip()
        password = request.POST.get("password", '')
        if nick == "" or password == "":
            data = {"nick":nick, "msg": '请输入用户名或密码'}
            return render(request,"user/login.html", data)
        user = authenticate(nick=nick, password=password)
        if user:
            auth.login(request, user)

            rn = request.session.get('next_page', '')
            if rn:
                if rn.replace("https?://", "") == request.get_host() + "/":
                    return HttpResponseRedirect(rn)
            return HttpResponseRedirect(request.session.get('next_page', reverse("index")))
        else:
            data={"nick": nick, "msg": '账号或密码错误'}
            return render(request,"user/login.html", data)
