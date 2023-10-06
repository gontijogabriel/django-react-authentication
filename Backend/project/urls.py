from setup.urls import path, include
from project.views import login, index, register

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('captcha/', include('captcha.urls')),
]