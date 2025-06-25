from django.urls import path

from OtidiDo.ideas.views import create_idea, edit_idea, delete_idea, IdeaDetailView, like_idea, search_view

urlpatterns = [
    path('create/', create_idea, name='create_idea'),
    path('<int:pk>', IdeaDetailView.as_view(), name='idea_detail'),
    path('<int:pk>/edit/', edit_idea, name='edit_idea'),
    path('<int:pk>/delete', delete_idea, name='delete_idea'),
    path('<int:pk>/like/', like_idea, name='like_idea'),
    path("search/", search_view, name="search"),
]
