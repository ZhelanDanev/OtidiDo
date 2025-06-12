from django.urls import path

from OtidiDo.common.views import home

urlpatterns = [
    path('', home, name='home'),
]
