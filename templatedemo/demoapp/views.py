from django.shortcuts import render
import datetime

# Create your views here.
def display(request):
    date=datetime.datetime.now()
    name="manic"
    date_dict={"display_date":str(date),"myname":name}
    return render(request,"demoapp/index.html",context = date_dict)
