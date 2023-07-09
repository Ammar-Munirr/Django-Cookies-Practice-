from django.shortcuts import render

# Create your views here.
def set_signed_cookie(request):
    res = render(request,'signed_cookie/set.html')
    res.set_signed_cookie('name',"Ammar",salt='Am')
    return res
def get_signed_cookie(request):
    name = request.get_signed_cookie('name',salt='Am',default='Not Found')  # salt is the signature to identify the cookie
    return render(request,'signed_cookie/get.html',{'name':name})

def delete_signed_cookie(request):
    res = render(request,'signed_cookie/delete.html')
    res.delete_cookie('name')
    return res