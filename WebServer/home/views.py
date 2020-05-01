from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Loaisp, SanPham, SPBan

# Create your views here.

class HomeView(View):
    def get(self,request):
        a = SPBan.objects.all()
        c= Loaisp.objects.all()
        return render(request, 'home/home.html',{'f':a,'nav':'home','loai':c})
