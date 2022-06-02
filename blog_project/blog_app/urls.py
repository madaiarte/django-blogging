from django.urls import path
from blog_app import views

urlpatterns = [
    path("about", views.AboutView.as_view(), name="about"),
    path("<int:pk>", views.BlogDetailView.as_view(), name="blog_detail"),
    path("new/", views.CreateBlogView.as_view(), name="blog_new"),
    path("<uuid:pk>/edit/", views.BlogUpdateView.as_view(), name="blog_edit"),
    path("<uuid:pk>/delete/", views.BlogUpdateView.as_view(), name="blog_remove"),
    path("drafts/", views.DraftListView, name="blog_draft_lists"),
    path("<int:pk>/comment", views.add_comment_to_post, name="add_comment_to_post"),
    path("comment/<int:pk>/approve", views.comment_approve, name="comment_approve"),
    path("comment/<int:pk>/remove", views.comment_remove, name="comment_remove"),
    path("<uuid:pk>/publish", views.blog_publish, name="blog_publish"),    
]
