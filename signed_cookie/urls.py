from django.urls import path
from . import views

urlpatterns = [
    path('set/',views.set_signed_cookie,name='set_signed'),
    path('get/',views.get_signed_cookie,name='get_signed'),
    path('delete/',views.delete_signed_cookie,name='delete_signed')
]
