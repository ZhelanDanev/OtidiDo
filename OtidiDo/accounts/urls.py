from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from OtidiDo.accounts.views import register, profile, edit_profile

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile')

]
