from django.shortcuts import render
from django.views import generic
from .models import IndexInfo, BlogPost, Comment, Blogger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


def index(request):
    # gets the first object from the model and their field
    title = IndexInfo.objects.first().title
    description = IndexInfo.objects.first().description

    context = {
        "title": title,
        "description": description,
    }

    return render(request, "index.html", context=context)


class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 10


class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 10


def BlogPostDetailView(request, pk):
    post = BlogPost.objects.get(pk=pk)
    comments = post.comment_set.all()
    return render(
        request, "blog_app/blogpost_detail.html", {"post": post, "comments": comments}
    )


def BloggerDetailView(request, pk):
    blogger = Blogger.objects.get(pk=pk)
    posts = blogger.blogpost_set.all()
    return render(
        request, "blog_app/blogger_detail.html", {"blogger": blogger, "posts": posts}
    )
