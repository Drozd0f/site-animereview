from django.urls import path

from . import views

urlpatterns = [
    path('', views.ReviewsHome.as_view(), name='index'),
    path('temp/', views.temp, name='temp'),
    path('addpage/', views.AddPage.as_view(), name='add_post'),
    path('user/update/<int:pk>', views.UserUpdateProfile.as_view(), name='profile_update'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('genre/<int:genre_id>/', views.PostGenre.as_view(), name='genre'),
]

