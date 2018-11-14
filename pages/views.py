from django.http import HttpResponse
from django.shortcuts import render
from tkinter import *


# Create your views here.

def home(request):
#tu beda pola do korych wpisujemy dane
#przyciski ktore zatwierdzzaja
#okno w ktorym ma sie otworzyc drzewko

#wszystgkie elementy zapisujemy w jednym bloku zeby wywoal go jako jedna zmienna w nawiasach {}
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

def image(request):
    return render(request, "image.html", {})

def contact(request):
    return render(request, "contact.html", {})

def profile(request):
    return render(request, "profile.html", {})





