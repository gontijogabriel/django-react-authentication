from setup.urls import path, include
from project.views import login, index

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('captcha', include('captcha.urls'))
]