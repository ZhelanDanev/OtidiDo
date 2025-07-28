from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from OtidiDo.accounts.views import register, profile, edit_profile, delete_profile, profile_detail

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/<int:pk>/', profile_detail, name='profile_detail'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('delete-profile/', delete_profile, name='delete_profile')


]
