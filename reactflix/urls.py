from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import RegisterUser
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Default admin page
    path('admin/', admin.site.urls),
    # Resources
    path('api/videos/', include('videos.urls')),
    path('api/categories/', include('categories.urls')),
    # Authentication
    path('api/auth/sign-up/', RegisterUser.as_view()),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
