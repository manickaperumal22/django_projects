from django.shortcuts import render
from crudapp.models import student
# Create your views here.

def retrieve_view(request):
    stud=student.objects.all()
    return render(request,"crudapp/index.html",{"student":stud})
