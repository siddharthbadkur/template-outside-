 

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home2(request):
    return render(request,('app2/home.html'))
