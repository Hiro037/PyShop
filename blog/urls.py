from django.urls import path
from blog.apps import BlogConfig
from blog.views import (
    BlogPostListView,
    BlogPostDetailView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("blogs/", BlogPostListView.as_view(), name="BlogPostList"),
    path("blogs/main", BlogPostListView.as_view(), name="BlogPostListMain"),
    path("blogs/<int:pk>/", BlogPostDetailView.as_view(), name="BlogPostDetail"),
    path("blogs/create-post/", BlogPostCreateView.as_view(), name="BlogPostCreate"),
    path("blogs/<int:pk>/update/", BlogPostUpdateView.as_view(), name="BlogPostUpdate"),
    path("blogs/<int:pk>/delete/", BlogPostDeleteView.as_view(), name="BlogPostDelete"),
]
