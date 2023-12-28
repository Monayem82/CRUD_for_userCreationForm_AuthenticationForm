from django.urls import path
from . import views

urlpatterns = [
    path('singup/',views.signUpHome,name='joinus'),
    path('login/',views.loginUsers,name='loginUser'),
    path('success/',views.successfully,name='suc'),
    path('logout/',views.logOut,name='logout_set'),
    path('createUser/',views.newUser,name='createUser'),
    path('cwithold/',views.cpasswithOld,name='changepasswithold'),
    path('changeProfile/',views.changeInfoPer,name='changeInformation'),
    path('showalldata/',views.dataTable,name="showJoin"),
    path('delete/<id>/',views.deleteJoiner),

]
