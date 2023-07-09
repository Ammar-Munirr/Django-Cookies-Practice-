from django.shortcuts import render

# Create your views here.
def set_cookie(request):
    res = render(request,'simple_cookie/set.html')
    res.set_cookie('name','Ammar')
    return res


def get_cookie(request):
    name = request.COOKIES.get('name','Not Found')
    return render(request,'simple_cookie/get.html',{'name':name})