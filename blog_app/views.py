from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from .models import IndexInfo, BlogPost, Comment, Blogger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import CommentForm
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


def index(request):
    # gets the first object from the model and their field
    title = IndexInfo.objects.first().title
    description = IndexInfo.objects.first().description

    context = {"title": title, "description": description}

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


@login_required
def AddComment(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog_post = post
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = CommentForm()
    return render(request, "blog_app/add_comment.html", {"form": form, "post": post})


# class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
# model = BlogPost
# permission_required = "blog_app.is_blogger"
# fields = ["title", "body"]


class PostCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ["title", "body"]
    success_url = reverse_lazy("posts")
    permission_required = "blog_app.is_blogger"

    def form_valid(self, form):
        # searched the for Blogger objects with a user what is currently logged in
        blogger = Blogger.objects.get(user=self.request.user)
        # modifies the current form with a value
        form.instance.author = blogger
        return super().form_valid(form)
