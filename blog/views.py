from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from blog.models import BlogPost


class BlogPostListView(ListView):
    # Главная страница со всеми постами
    model = BlogPost


class BlogPostDetailView(DetailView):
    # Страница с отображением информации об одном посте
    model = BlogPost

    def get_object(self, queryset=None):
        # Увеличивает счетчик просмотров на 1 при просмотре страницы
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    # Страница создания поста
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]
    success_url = reverse_lazy("blog:BlogPostListMain")


class BlogPostUpdateView(UpdateView):
    # Страница изменения поста
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]

    def get_success_url(self):
        # Возвращает на сайт поста после его изменения
        return reverse_lazy("blog:BlogPostDetail", args=[self.kwargs.get("pk")])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog:BlogPostListMain")
