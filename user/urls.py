from django.urls import path
from .views import (
    User, UserDetail, 
    UserCreate, UserUpdate, UserDelate
    )


urlpatterns = [
    path('users/', User.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('users/create/', UserCreate.as_view()),
    path('users/<int:pk>/update/', UserUpdate.as_view()),
    path('users/<int:pk>/delete/', UserDelate.as_view()),
]