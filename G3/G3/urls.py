from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('generic/', include('geekapp.urls')),
    path('concrete/', include('concrete.urls')),
    path('newset/', include('newset.urls')),

    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
     path('api/gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]
    
    

