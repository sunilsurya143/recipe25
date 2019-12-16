from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api import TestView, UserView,UserProfileView, StudentView

urlpatterns = [
    path('test/', TestView.as_view()),
    path('user/', UserView.as_view()),
    path('user/<int:pk>/', UserView.as_view()),
    path('userpro/', UserProfileView.as_view()),
    path('userpro/<int:pk>/', UserProfileView.as_view()),
    path('student/', StudentView.as_view()),
    path('student/<int:pk>/', StudentView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)