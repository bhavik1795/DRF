from django.contrib import admin
from django.urls import path
from proapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.student_api),        #----> For Function Based View
    path('studentapi/<int:pk>', views.student_api),
    
    # path('studentapi/', views.StudentAPI.as_view()),    #----> For Class Based View
    # path('studentapi/<int:pk>', views.StudentAPI.as_view())
]
