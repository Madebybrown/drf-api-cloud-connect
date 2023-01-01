from django.urls import path
from userprofiles import views

urlpatterns = [
    path('userprofiles/', views.ProfileList.as_view()),
    path('userprofiles/<int:pk>/', views.ProfileDetail().as_view()),
]