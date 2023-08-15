from decouple import config
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def salir(request):
    logout(request)
    return redirect('login')

@login_required
def inicio(request):
    provident_apis = config("APIS_PROVIDENT")
    return render(request, "inicio/inicio.html",{'provident_apis':provident_apis})
