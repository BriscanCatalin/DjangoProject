from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'chat'
urlpatterns = [
    path('', views.login_view, name="login"),
    url(r'home', views.home, name='home'),
    url(r'logout', views.logout_user, name='logout'),
    path('<str:room>/', views.room, name="room"),
    path('checkview', views.checkview, name="checkview"),
    path('send', views.send, name="send"),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages"),
]