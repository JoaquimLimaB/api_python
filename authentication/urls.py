from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# 150; Documentação SimpleJWT: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html (Para autemticações de API)
urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('authentication/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('authentication/token/verify/',
         TokenVerifyView.as_view(), name='token_verify'),
]
