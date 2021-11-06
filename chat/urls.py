from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'chat'
urlpatterns = [
    path('', views.login_view, name="login"),
    path('home', views.home, name="home"),
    path('logout', views.logout_user, name="logout"),
    path('register', views.register, name="register"),
    path('<str:room>/', views.room_, name="room"),
    path('checkview', views.checkview, name="checkview"),
    path('send', views.send, name="send"),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages"),
]