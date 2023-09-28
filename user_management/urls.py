from django.urls import path
from . import views

urlpatterns = [
    path('user/create/', views.create_user, name='create_user'),
    path('user/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('user/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('user/list/', views.user_list, name='user_list'),
]
