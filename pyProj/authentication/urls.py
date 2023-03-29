from django.urls import path
from .views import sign_up, post_list, post_detail, post_new, post_edit

app_name = 'authentication'

urlpatterns = [
    path('sign-up/', sign_up, name='sign_up'),
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
]