from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:user_name>/', views.user_detail, name='detail'),
    path('signup/', views.SignupView.as_view(), name='signup'),
]
