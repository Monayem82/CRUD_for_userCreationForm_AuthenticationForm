from django.shortcuts import render
from singup_in.forms import makePersonalDetails
from django.http import HttpResponseRedirect


# Create your views here.
def funHome(request):
    return render(request,'home/home.html')

# def showJoinAll(request):
#     # if request.user.is_authenticated:
#     #     if request.method=='POST':
#     #         frm=makePersonalDetails(request.POST)
#     #         if frm.is_valid():
#     #             frm.save()
#     #             return HttpResponseRedirect('/join/success/')
#     #     else:
#     #         frm=makePersonalDetails()
#     #     templete_vari={
#     #         "form":frm
#     #     }
#     #     return render(request,'singup_in/changeInfoPerhtml.html',templete_vari)
#     return render(request,'home/showall.html')