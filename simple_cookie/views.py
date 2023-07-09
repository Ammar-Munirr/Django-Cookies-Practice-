from django.shortcuts import render

# Create your views here.
def set_cookie(request):
    res = render(request,'simple_cookie/set.html')
    res.set_cookie('name','Ammar')
    return res