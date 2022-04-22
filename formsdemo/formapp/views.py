from django.shortcuts import render
from . import forms
# Create your views here.
def empDetailsView(request):
    form=forms.employeeInfoForm()
    empinfo={"form":form}
    return render(request,"formapp/form.html",context=empinfo)