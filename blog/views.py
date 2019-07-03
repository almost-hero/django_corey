from django.shortcuts import render
from .models import *

# Create your views here.
def home_page(request):
    context = { 'posts': Post.objects.all()}
    return render(request,'blog/home_page.html',context)

def about_page(request):
    return render(request,'blog/about_page.html')
