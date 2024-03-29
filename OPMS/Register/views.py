from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse
from . import forms
import bcrypt
from django.contrib.auth import get_user_model;
from Register.models import Doc,Patient
User = get_user_model();

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = '/login'
    template_name = 'signup.html'
def index(request):
    return render(request, 'main.html')
def appoinment(request):
    return render(request,'appointments.html')
def p_inform(request):
    u = User.objects.get(username=request.user.get_username())
    patient = Patient.objects.get_or_create(patient=u)[0];
    return render(request,'patient_information')
def homePage(request):
    user=User
    print(type(User))
    docc = Doc.objects.order_by()
    print(type(docc[0]))
    isDoc = False
    n = User.objects.get(username=request.user.get_username())
    for i in docc:
        doctor = i.doc
        if (str(n) == str(doctor.username)):
            isDoc = True
            break

    if (isDoc):
        return render(request,'success.html')
    else:
        u = User.objects.get(username=request.user.get_username())
        patient = Patient.objects.get_or_create(patient=u)[0];
        c = {'patient':patient}
        return render(request,'homePage.html',c)
