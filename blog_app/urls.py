from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.BlogPostListView.as_view(), name="posts"),
    path("bloggers/", views.BloggerListView.as_view(), name="bloggers"),
    path("post/<int:pk>", views.BlogPostDetailView, name="post-detail"),
    path("blogger/<int:pk>", views.BloggerDetailView, name="blogger-detail"),
]
