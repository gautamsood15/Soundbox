from django.shortcuts import render

# Create your views here.
def index(request):
    now = 
    context = {"var": "now"}
    return render(request, "index.html", context)