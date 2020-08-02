from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCreateCategories.as_view()),
    path('videos/', views.ListCategoriesWithVideos.as_view()),
    path('<int:pk>/', views.RetrieveUpdateDestroyCategories.as_view()),
    path('<int:pk>/videos/', views.ListCategorieVideos.as_view()),
]