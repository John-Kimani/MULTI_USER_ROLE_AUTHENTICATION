from django.urls import path
from . import views

urlpatterns = [
    path('', views.HelloAuthView.as_view(), name='hello_auth'),
    path('register/', views.SignUpUserView.as_view(), name='sign_up'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('me/', views.RetrieveUserView.as_view()),
]
