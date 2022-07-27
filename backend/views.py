from django.shortcuts import render

# Create your views here.
def Dashboard(request):
    return render(request, "index.html")