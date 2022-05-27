import uuid

# from django.core import validators
from django.db import models

# from django_countries.fields import CountryField
from django.utils import timezone
from django.urls import reverse

# Create your models here.


# class UsersModel(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     country = CountryField()
#     email = models.EmailField(unique=True)
#     password = models.CharField(
#         max_length=30,
#         validators=[
#             validators.MinLengthValidator(5, "It should contain at least 5 characters"),
#             validators.RegexValidator(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W)"),
#         ],
#     )


class CategoriesModel(models.Model):
    category_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.category_name


class BlogsModel(models.Model):
    TYPE_BLOG_CHOICES = [
        ("VD", "Video Blog"),
        ("TX", "Text Blog"),
        ("AU", "Podcast Blog"),
        ("VR", "Virtual Blog"),
        ("OT", "Other Blog"),
    ]

    id = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4
    )
    title = models.CharField(
        max_length=512,
    )
    subtitle = models.TextField()
    liked_by = models.UUIDField(unique=True, editable=False, null=True)
    type_blog = models.CharField(max_length=2, choices=TYPE_BLOG_CHOICES)
    background = models.ImageField()
    create_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    # user = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.DO_NOTHING)
    category = models.OneToOneField(CategoriesModel, on_delete=models.CASCADE)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comment.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.title


class CommentsModel(models.Model):
    user = models.UUIDField(editable=False)
    comment = models.TextField(null=True)
    create_date = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)
    blog = models.ForeignKey(
        BlogsModel, on_delete=models.CASCADE, related_name="comments"
    )
    comment_comment = models.ForeignKey("CommentsModel", on_delete=models.CASCADE)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("blog_list")

    def __str__(self):
        return self.comment


class BlogSectionsModel(models.Model):
    TYPE_BLOG_SECTIONS_CHOICES = [
        ("1", "total"),
        ("2", "2:1"),
        ("3", "1:2"),
        ("4", "1:1:1"),
    ]
    type = models.CharField(max_length=1, choices=TYPE_BLOG_SECTIONS_CHOICES)
    content = models.TextField(null=True)
    blog = models.ForeignKey(BlogsModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.type


class BlogSectionImagesModel(models.Model):
    image = models.ImageField(null=True)
    blog_section = models.ForeignKey(BlogSectionsModel, on_delete=models.CASCADE)
