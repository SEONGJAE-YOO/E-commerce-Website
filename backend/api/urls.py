from django.urls import path
from userauths import views as userauths_views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('user/token/', userauths_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/register/', userauths_views.RegisterView.as_view(), name='auth_register'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]