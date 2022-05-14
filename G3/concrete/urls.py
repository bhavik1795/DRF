from django.urls import path
from concrete import views

urlpatterns = [
    path('stuapi/l/', views.StudentList.as_view()),
    path('stuapi/c/', views.StudentCreate.as_view()),
    path('stuapi/r/<int:pk>', views.StudentRetrieve.as_view()),
    path('stuapi/u/<int:pk>', views.StudentUpdate.as_view()),
    path('stuapi/d/<int:pk>', views.StudentDestroy.as_view()),
    path('stuapi/lc/', views.StudentListCreate.as_view()),
    path('stuapi/ru/<int:pk>', views.StudentRetrieveUpdate.as_view()),
    path('stuapi/rd/<int:pk>', views.StudentRetrieveDestroy.as_view()),
    path('stuapi/rud/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),

]