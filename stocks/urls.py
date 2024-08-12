from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('sector/<slug:slug>/', views.sector_detail, name='sector_detail'),
    # path('sector_analysis/', views.sector_analysis, name='sector_analysis'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('articles/', views.article_list, name='article_list'),  # Ensure this pattern exists
    path('login/', views.login_view.as_view(), name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.user_profile, name='user_profile'),
    path('logout/', views.logout_view, name='logout')
]