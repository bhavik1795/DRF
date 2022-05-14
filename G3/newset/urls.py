from django.urls import path, include
from newset import views
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
# router.register(r'studentapi', views.StudentViewSet, basename='student')
router.register(r'studentmodelapi', views.StudentModelViewset, basename='studentmodel')
# router.register(r'studentromapi', views.StudentRomViewset, basename='studentrom')

urlpatterns = [
    path('api/', include(router.urls)),
    # path('api/gettoken/', obtain_auth_token),
    # path('gettoken/', obtain_auth_token)
   ]