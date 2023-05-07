from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    return HttpResponse("<h1>Women Page</h1>")

def categories(request,catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Category number: </h1> <p>{catid}</p>")

def arhive(request,year):
    if int(year)> 2023:
        return redirect('home',permanent=True)
    
    return HttpResponse(f"<h1>{year}</h1>")

def pageNotFound(request,exception):
    return HttpResponseNotFound(f"<h1>Page not found( foggot))</h1>")