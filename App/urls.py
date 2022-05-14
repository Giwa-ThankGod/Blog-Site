from django.urls import path, include
from App import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('Post/<category>/', views.Categories, name='category'),
    path('<category>/<slug>/', views.Detail, name='detail'),
    path('<category>/<slug>/<comment_id>', views.Reply, name='Reply'),
    path('Get/Comment/<id>/', views.GetComment, name='GetComment'),
    path('get/Replies/<id>/', views.getReplies, name='getReplies'),
    path('About/', views.About, name='about'),
    path('Contacts/', views.Contact, name='contact'),
]