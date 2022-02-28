from django.urls import path
from Boomie import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<category>/<slug>/', views.detail, name='detail'),
    path('<category>/', views.category, name='cat'),
    path('<category>/<slug>/<id>/', views.reply, name='reply'),
]