from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCreateVideos.as_view()),
    path('<int:pk>/', views.RetrieveUpdateDeleteVideos.as_view()),
]
