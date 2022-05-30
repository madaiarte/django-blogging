from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse_lazy
from blog_app.models import BlogsModel, CommentsModel
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blog_app.forms import BlogsForm
from blog_app.forms import CommentsForm


# Create your views here.


class AboutView(TemplateView):
    template_name: str = "about.html"


class HomeView(ListView):
    model = BlogsModel
    template_name = "home.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return BlogsModel.objects.filter(publish_date__lte=timezone.now()).order_by(
            "-publish_date"
        )


class BlogDetailView(DetailView):
    model = BlogsModel


class CreateBlogView(LoginRequiredMixin, CreateView):
    login_url = "/login"
    redirect_field_name = "blog_app/blog_detail.html"
    form_class = BlogsForm
    model = BlogsModel


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login"
    redirect_field_name = "blog_app/blog_detail.html"
    form_class = BlogsForm
    model = BlogsModel


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login"
    success_url = reverse_lazy("blog_list")


class DraftListView(LoginRequiredMixin, ListView):
    login_url = "/login"
    redirect_field_name = "blog_list.html"
    model = BlogsModel

    def get_queryset(self):
        return BlogsModel.objects.filter(published_date__isnull=True).order_by(
            "created_date"
        )


#
#


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(BlogsModel, pk=pk)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", pk=post.pk)
        else:
            form = CommentsForm()
    return render(request, "blog_app/comment_form.html", {"form": form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(CommentsModel, pk=pk)
    comment.approve()
    return redirect("post_detail", pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(CommentsModel, pk=pk)
    blog_pk = comment.post.pk  # Saves the pk before deleted
    comment.delete()

    return redirect("post_detail", pk=blog_pk)


@login_required
def blog_publish(request, pk):
    blog = get_object_or_404(BlogsModel, pk=pk)
    blog.publish()
    return redirect("blog_detail")
