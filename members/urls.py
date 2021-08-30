from django.urls import path
from .views import UserCreationView

urlpatterns = [
    #path('login/', UserLoginView.as_view(), name="login"),
    path('register/', UserCreationView.as_view(), name="register"),


]
