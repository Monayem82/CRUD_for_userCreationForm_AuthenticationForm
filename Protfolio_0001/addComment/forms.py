from django import forms

class makePost(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    topic_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    describe=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    