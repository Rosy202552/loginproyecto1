from django.urls import path
from .views import login_view, home

urlpatterns = [
    path('', home),
    path('login/', login_view),
]