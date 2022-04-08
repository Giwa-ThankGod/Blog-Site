from django.urls import path, include
from users import views

urlpatterns = [
    # path('', include("django.contrib.auth.urls")),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
]