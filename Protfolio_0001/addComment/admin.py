from django.contrib import admin
from .models import addComment



class addCommnetAdmin(admin.ModelAdmin):
    list_display=('id','name','email','topic_name','describe')

admin.site.register(addComment,addCommnetAdmin)