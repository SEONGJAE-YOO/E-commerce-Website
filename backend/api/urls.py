from django.urls import path
from userauths import views as userauths_views
from rest_framework_simplejwt.views import TokenRefreshView
from store import views as store_views


urlpatterns = [
    path('user/token/', userauths_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/register/', userauths_views.RegisterView.as_view(), name='auth_register'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/password-reset/<email>/', userauths_views.PasswordEmailVerify.as_view(), name='password_reset'),
    path('user/password-change/', userauths_views.PasswordChangeView.as_view(), name='password_change'),


    #Store Endpoints
    path('category/',  store_views.CategoryListAPIView.as_view(), name='category_list'),
    path('product/',  store_views.ProductListAPIView.as_view(), name='product_list'),
    path('product/<slug>/',  store_views.ProductDetailAPIView.as_view(), name='product-detail'),

]