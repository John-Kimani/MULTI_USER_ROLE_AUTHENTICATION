from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="MultiUser Authenticaton API",
      default_version='v1',
      description="A REST API for user authentication system",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kimperriatest@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('authentication.urls')),
   #  path('auth/', include('djoser.urls.jwt')),
   path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
                          
    #swagger
    path('swagger<format>.json.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
