from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"var": "Website is deployed with custom domain"}
    return render(request, 'index.html', context)