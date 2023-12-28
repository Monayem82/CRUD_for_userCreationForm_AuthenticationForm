from django.shortcuts import render,HttpResponse
from .forms import createUserusingCreationForm,passChangewithOldp,modifyUser,loginForms
from django.http import HttpResponseRedirect
from singup_in.forms import makePersonalDetails
from singup_in.models import makePersionalDe
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.core import validators

# Create your views here.
def signUpHome(request):
    if request.method=='POST':
        frm=makePersonalDetails(request.POST)
        if frm.is_valid():
            fname=frm.cleaned_data['name']
            email=frm.cleaned_data['email']

            dbemail=makePersionalDe.objects.all()
            for dbe in dbemail:
                if email !=dbe.email:
                    pass
                else:
                    values=0
                    return HttpResponse('This email is exits in database try another')

            department=frm.cleaned_data['department']
            code=frm.cleaned_data['dep_code']
            psw=frm.cleaned_data['password']
            sqls=makePersionalDe(name=fname,email=email,department=department,dep_code=code,password=psw)
            sqls.save()
            return HttpResponseRedirect('/home/')


    else:
        frm=makePersonalDetails()
    gohtmlfile={
        "form":frm,
    }
    return render(request,'singup_in/signup.html',context=gohtmlfile)

# CRUD Operations

def dataTable(request):
    data=makePersionalDe.objects.all()
    return render(request,'home/showall.html',{"data":data})

def deleteJoiner(request,id):
    data=makePersionalDe.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect('/join/showalldata/')

# close CRUD Operations

def loginUsers(request):
    if request.method == 'POST':
        frm=loginForms(request=request,data=request.POST)
        if frm.is_valid():
            usern=frm.cleaned_data['username']
            psw=frm.cleaned_data['password']
            print(usern,psw)
            user=authenticate(username=usern,password=psw)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/join/success/')
    else:
        frm=loginForms()
    templeVariable={
        "form":frm,
    }
    return render(request,'singup_in/login.html',templeVariable)


# login successfully sms

def successfully(request):
    if request.user.is_authenticated:
        frm=modifyUser(instance=request.user)
        templete_vari={
            "form":frm
        }
        return render(request,'singup_in/loginsuccess.html',templete_vari)

# infomation change 
def changeInfoPer(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            frm=modifyUser(request.POST,instance=request.user)
            if frm.is_valid():
                frm.save()
                return HttpResponseRedirect('/join/success/')
        else:
            frm=modifyUser(instance=request.user)
        templete_vari={
            "form":frm
        }
        return render(request,'singup_in/changeInfoPerhtml.html',templete_vari)




def logOut(request):
    logout(request)
    return HttpResponseRedirect('/join/login/')

# Creating User For django database

def newUser(request):
    if request.method == 'POST':
        frm=createUserusingCreationForm(request.POST)
        if frm.is_valid():
            frm.save()
            return HttpResponseRedirect('/join/login/')
    else:
        frm=createUserusingCreationForm()

    temple_variable={
        "form":frm,
    }
    return render(request,'singup_in/usercreate.html',temple_variable)

# password change Form
# def cpasswithOld(request):
#     frm=passChangewithOldp
#     htmlVariable={
#         "form":frm,
#     }
#     return render(request,'singup_in/changewithOld.html',htmlVariable)

def cpasswithOld(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            frm=passChangewithOldp(user=request.user,data=request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request,frm.user)
                return HttpResponseRedirect('/join/success/')      
        else:
            frm=passChangewithOldp(user=request.user)
        htmlVariable={
            "form":frm,
        }
        return render(request,'singup_in/changewithOld.html',htmlVariable)
    else:
        return HttpResponseRedirect('/join/login/')