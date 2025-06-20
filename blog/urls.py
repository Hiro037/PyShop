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
    path("", BlogPostListView.as_view(), name="BlogPostList"),
    path("main/", BlogPostListView.as_view(), name="BlogPostListMain"),
    path("<int:pk>/", BlogPostDetailView.as_view(), name="BlogPostDetail"),
    path("create-post/", BlogPostCreateView.as_view(), name="BlogPostCreate"),
    path("<int:pk>/update/", BlogPostUpdateView.as_view(), name="BlogPostUpdate"),
    path("<int:pk>/delete/", BlogPostDeleteView.as_view(), name="BlogPostDelete"),
]
