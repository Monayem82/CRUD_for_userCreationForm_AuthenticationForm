from django.shortcuts import render

# Create your views here.
def gellaryMain(request):
    return render(request,'gellary/gellaryMain.html')