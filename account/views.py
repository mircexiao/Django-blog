from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegistrationForm,UserProfileForm,UserInfoForm,UserForm
from django.contrib.auth.decorators import login_required
from.models import UserInfo,UserProfile
from django.http import HttpResponseRedirect

# Create your views here.
def user_login(request):
    if request.method=="POST":
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            cd=login_form.cleaned_data
            user=authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse("登录成功")
            else:
                return HttpResponse("密码错误")
        else:
            return HttpResponse("请输入正确的账号或密码")
    if request.method=="GET":
        login_form=LoginForm()
        return render(request,"account/login.html",{"form":login_form})

def register(request):
    if request.method=='POST':
        user_form=RegistrationForm(request.POST)
        userprofile_form=UserProfileForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile=userprofile_form.save(commit=False)
            new_profile.user=new_user
            new_profile.save()
            return HttpResponse('注册成功')
        else:
            return HttpResponse('注册失败')
    else:
        user_form=RegistrationForm()
        userprofile_form=UserProfileForm()
        return render(request,"account/register.html",{"form":user_form,"profile":userprofile_form})

@login_required()
def myself(request):
    userprofile=UserProfile.objects.get(user=request.user) if hasattr(request.user,'userprofile') else UserProfile.objects.create(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user,'userinfo') else UserInfo.objects.create(user=request.user)
    return render(request,"account/myself.html",{
        "user": request.user,
        "userinfo": userinfo,
        "userprofile": userprofile
    })

@login_required(login_url='/account/login/')
def myself_edit(request, ):
    userprofile=UserProfile.objects.get(user=request.user) if hasattr(request.user,'userprofile') else UserProfile.objects.create(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user,'userprofile') else UserInfo.objects.create(user=request.user)

    if request.method=="POST":
        user_form=UserForm(request.POST)
        userprofile_form=UserProfileForm(request.POST)
        userinfo_form=UserInfoForm(request.POST)
        if user_form.is_valid() and userprofile_form.is_valid() and userinfo_form.is_valid():
            user_cd=user_form.cleaned_data
            userprofile_cd=userprofile_form.cleaned_data
            userinfo_cd=userinfo_form.cleaned_data
            request.user.email=user_cd['email']
            userprofile.birth=userprofile_cd['birth']
            userprofile.phone=userprofile_cd['phone']
            userinfo.school=userinfo_cd['school']
            userinfo.company=userinfo_cd['company']
            userinfo.profession=userinfo_cd['profession']
            userinfo.address=userinfo_cd['address']
            userinfo.about_me=userinfo_cd['about_me']
            request.user.save()
            userprofile.save()
            userinfo.save()
        return HttpResponseRedirect('/account/my-information/')
    else:
        user_form=UserForm(instance=request.user)
        userprofile_form=UserProfileForm(initial={
            'birth':userprofile.birth,
            'phone':userprofile.phone
        })
        userinfo_form=UserInfoForm(initial={
            'school':userinfo.school,
            'company':userinfo.company,
            'profession':userinfo.profession,
            'address':userinfo.address,
            'about_me':userinfo.about_me
        })
        return render(request,"account/myself_edit.html",{
            "user_form":user_form,
            "userprofile_form":userprofile_form,
            "userinfo_form":userinfo_form
        })

def my_image(request):
    return render(request,'account/imagecrop.html',)

@login_required(login_url='/account/login/')
def my_image(request):
    if request.method=="POST":
        img=request.POST['img']
        userinfo=UserInfo.objects.get(user=request.user.id)
        userinfo.photo=img
        userinfo.save()
        return HttpResponse("1")
    else:
        return render(request,'account/imagecrop.html')