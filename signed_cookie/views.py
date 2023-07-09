from django.shortcuts import render

# Create your views here.
def set_signed_cookie(request):
    res = render(request,'signed_cookie/set.html')
    res.set_signed_cookie('name',"Ammar",salt='Am')
    return res