from django.urls import path

from api import views

urlpatterns = [path('ping/', views.PingView.as_view()), ]
