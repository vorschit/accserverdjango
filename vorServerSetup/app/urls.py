from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from app import views
app_name = 'app'
urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('logout/',views.user_logout, name='logout'),
    path('home/',views.home,name='home'),
    path('genjson/',views.generated_json,name='generated_json' ),
]