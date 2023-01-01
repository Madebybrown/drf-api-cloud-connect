from django.urls import path
from userprofiles import views

urlpatterns = [
    path('userprofiles/', views.ProfileList.as_view()),
]