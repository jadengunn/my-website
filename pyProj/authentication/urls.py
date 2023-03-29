from django.contrib import admin
from django.urls import path, include
from .views import sign_up, post_list, post_detail, post_new, post_edit
from authentication.views import signup_view, login_view

app_name = 'authentication'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/signup/', signup_view, name='signup'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]