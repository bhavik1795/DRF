from django.contrib import admin
from django.urls import path, include
from geekapp import views


urlpatterns = [
    # path('stuapi/', views.StudentList.as_view()),
    # path('stuapi/', views.StudentCreate.as_view()),
    # path('stuapi/<int:pk>', views.StudentRetrive.as_view()),
    # path('stuapi/<int:pk>', views.StudentUpdate.as_view()),
    # path('stuapi/<int:pk>', views.StudentDestroy.as_view()),
    path('stuapi/', views.LCStudentAPI.as_view()),
    # path('stuapi/<int:pk>', views.RUDStudentAPI.as_view()),

]