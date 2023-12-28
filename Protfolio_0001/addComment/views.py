from django.shortcuts import render
from .forms import makePost
from .models import addComment
from django.http import HttpResponse,HttpResponseRedirect


def commenter(request):
    if request.method=="POST":
        frm=makePost(request.POST)
        if frm.is_valid():
            nameu=frm.cleaned_data['name']
            emailu=frm.cleaned_data['email']
            topicn=frm.cleaned_data['topic_name']
            desc=frm.cleaned_data['describe']
            queryset=addComment(name=nameu,email=emailu,topic_name=topicn,describe=desc)
            queryset.save()
            return HttpResponseRedirect('/comment/')

    else:
        frm=makePost()
    
    data =addComment.objects.all()
    return render(request,'addComment/comment.html',context={"form":frm,"data":data})

def deleteComment(request,id):
    data=addComment.objects.get(id =id)
    data.delete()
    return HttpResponseRedirect('/comment/')

def updateComment(request,id):
    sqlset=addComment.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        nameu=data.get('name')
        emailu=data.get('email')
        topic=data.get('topic_name')
        descri=data.get('describe')

        sqlset.name=nameu
        sqlset.email=emailu
        sqlset.topic_name=topic
        sqlset.describe=descri
        sqlset.save()

        return HttpResponseRedirect('/comment/')
    return render(request,'addComment/update.html',context={"data":sqlset})