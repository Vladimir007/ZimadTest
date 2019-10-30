from django.urls import path
from users import views, api


urlpatterns = [
    path('', views.UserListView.as_view(), name='list'),
    path('create/', views.CreateUserView.as_view(), name='create'),

    path('api/list/', api.UserListAPIView.as_view(), name='api-list'),
    path('api/detail/<int:pk>/', api.UserDetailAPIView.as_view(), name='api-detail'),
]
