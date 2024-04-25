from django.shortcuts import render, HttpResponse

# Create your views here.



def index(request):
    return render(request, "index.html")


def maths(request):
    return render(request, "maths.html")


def science(request):
    return render(request, "science.html")


def coding(request):
    return render(request, "coding.html")


def sp(request):
    return render(request, "sp.html")



def contact(request):
    return render(request, "contact.html")



def cost(request):
    return render(request, "cost.html")


def b_a_teacher(request):
    return render(request, "b-a-teacher.html")



