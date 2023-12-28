from django.urls import path
from . import views

urlpatterns = [
    path('',views.funHome,name='homeps'),
    # path('showall',views.showJoinAll,name='showJoin'),
]
