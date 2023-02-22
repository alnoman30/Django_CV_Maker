import os

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import ResumeList


# Create your views here.
def base(request):
    return render(request, 'base.html')


def home(request):
    item = ResumeList.objects.filter(user=request.user)
    return render(request, 'home.html', locals())


def registration(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['conf_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email has been used')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, email=email,
                                                password=password, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                messages.success(request, 'Account successfully created')
                return redirect('login')
    return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login Success!")
            return redirect('home')
        else:
            messages.error(request, "Login failed!")
            return redirect('registration')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout success")
    return redirect('login')


def create(request):
    if request.method == 'POST':
        items = ResumeList()
        if len(request.FILES) != 0:
            items.profile_pic = request.FILES['images']
        items.title = request.POST.get('title')
        items.first_name = request.POST.get('first_name')
        items.last_name = request.POST.get('last_name')
        items.phone_number = request.POST.get('phone_number')
        items.email = request.POST.get('email')
        items.address = request.POST.get('address')
        items.skill_01 = request.POST.get('skill_01')
        items.skill_02 = request.POST.get('skill_02')
        items.skill_03 = request.POST.get('skill_03')
        items.skill_04 = request.POST.get('skill_04')
        items.skill_05 = request.POST.get('skill_05')
        items.skill_06 = request.POST.get('skill_06')
        items.award_01 = request.POST.get('award_01')
        items.award_02 = request.POST.get('award_02')
        items.award_03 = request.POST.get('award_03')
        items.award_04 = request.POST.get('award_04')
        items.award_05 = request.POST.get('award_04')
        items.language_01 = request.POST.get('language_01')
        items.language_02 = request.POST.get('language_02')
        items.profession = request.POST.get('profession')
        items.profile_detail = request.POST.get('profile_detail')
        items.job_title_01 = request.POST.get('job_title_01')
        items.j1_j_d = request.POST.get('j1_j_d')
        items.j1_l_d = request.POST.get('j1_l_d')
        items.job_details_01 = request.POST.get('job_details_01')
        items.job_title_02 = request.POST.get('job_title_02')
        items.j2_j_d = request.POST.get('j2_j_d')
        items.j2_l_d = request.POST.get('j2_l_d')
        items.job_details_02 = request.POST.get('job_details_02')
        items.job_title_03 = request.POST.get('job_title_03')
        items.j3_j_d = request.POST.get('j3_j_d')
        items.j3_l_d = request.POST.get('j3_l_d')
        items.job_details_03 = request.POST.get('job_details_03')
        items.school = request.POST.get('school')
        items.s_j_d = request.POST.get('s_j_d')
        items.s_l_d = request.POST.get('s_l_d')
        items.college = request.POST.get('college')
        items.c_j_d = request.POST.get('c_j_d')
        items.c_l_d = request.POST.get('c_l_d')
        items.university = request.POST.get('university')
        items.u_j_d = request.POST.get('u_j_d')
        items.u_l_d = request.POST.get('u_l_d')
        items.user = request.user
        items.save()
        return redirect('home')
    return render(request, 'create.html', locals())


def update(request, id):
    items = ResumeList.objects.get(id=id)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            items.profile_pic = request.FILES['images']
        items.title = request.POST.get('title')
        items.first_name = request.POST.get('first_name')
        items.last_name = request.POST.get('last_name')
        items.phone_number = request.POST.get('phone_number')
        items.email = request.POST.get('email')
        items.address = request.POST.get('address')
        items.skill_01 = request.POST.get('skill_01')
        items.skill_02 = request.POST.get('skill_02')
        items.skill_03 = request.POST.get('skill_03')
        items.skill_04 = request.POST.get('skill_04')
        items.skill_05 = request.POST.get('skill_05')
        items.skill_06 = request.POST.get('skill_06')
        items.award_01 = request.POST.get('award_01')
        items.award_02 = request.POST.get('award_02')
        items.award_03 = request.POST.get('award_03')
        items.award_04 = request.POST.get('award_04')
        items.award_05 = request.POST.get('award_04')
        items.language_01 = request.POST.get('language_01')
        items.language_02 = request.POST.get('language_02')
        items.profession = request.POST.get('profession')
        items.profile_detail = request.POST.get('profile_detail')
        items.job_title_01 = request.POST.get('job_title_01')
        items.j1_j_d = request.POST.get('j1_j_d')
        items.j1_l_d = request.POST.get('j1_l_d')
        items.job_details_01 = request.POST.get('job_details_01')
        items.job_title_02 = request.POST.get('job_title_02')
        items.j2_j_d = request.POST.get('j2_j_d')
        items.j2_l_d = request.POST.get('j2_l_d')
        items.job_details_02 = request.POST.get('job_details_02')
        items.job_title_03 = request.POST.get('job_title_03')
        items.j3_j_d = request.POST.get('j3_j_d')
        items.j3_l_d = request.POST.get('j3_l_d')
        items.job_details_03 = request.POST.get('job_details_03')
        items.school = request.POST.get('school')
        items.s_j_d = request.POST.get('s_j_d')
        items.s_l_d = request.POST.get('s_l_d')
        items.college = request.POST.get('college')
        items.c_j_d = request.POST.get('c_j_d')
        items.c_l_d = request.POST.get('c_l_d')
        items.university = request.POST.get('university')
        items.u_j_d = request.POST.get('u_j_d')
        items.u_l_d = request.POST.get('u_l_d')
        items.user = request.user
        items.save()
        messages.success(request, "Items has been Updated!")
        return redirect('home')

    return render(request, 'create.html', locals())


def view_cv(request, id):
    items = ResumeList.objects.get(id=id)
    return render(request, 'view_cv.html', locals())


def delete(request, id):
    items = ResumeList.objects.filter(id=id)
    items.delete()
    messages.success(request, "Items has been deleted!")
    return redirect('home')
