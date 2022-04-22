from django.shortcuts import render

# Create your views here.
# def cookies_count_view(request):
#     count=request.COOKIES.get("count",0)
#     totalcount=int(count)+1
#     response=render(request,"cookiesapp/index.html",{"count":totalcount})
#     response.set_cookie("count",totalcount)
#     return response

def cookies_count_view(request):
  count=request.session.get("count",0)
  totalcount=int(count)+1
  request.session['count']=totalcount
  return render(request,"cookiesapp/index.html",{'count':totalcount})