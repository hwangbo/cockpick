from django.urls import path
from . import views 

urlpatterns = [
    path('home/', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('bar/', views.bar, name='bar'),
    path('bar/<int:bar_id>/', views.bard, name='bard'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blog_id>/', views.detail, name='detail'),
    path('new/', views.blogpost, name='new'),
    path('', views.cock, name='cock'),
]