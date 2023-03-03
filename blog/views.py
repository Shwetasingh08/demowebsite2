from django.shortcuts import render

# Create your views here.
def home(request):
    author = 'shweta singh'
    age = 49
    address = 'sec-i'
    ctx = {'authr':author, 'age':age,'add':address}
    return render(request, 'home.html',content_type=ctx)