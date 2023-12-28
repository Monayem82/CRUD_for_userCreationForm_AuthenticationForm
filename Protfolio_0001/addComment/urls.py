from django.urls import path
from . import views
urlpatterns = [
    path('',views.commenter),
    path('delete/<id>/',views.deleteComment),
    path('update/<id>/',views.updateComment),
]
