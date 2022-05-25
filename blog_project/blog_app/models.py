import uuid
from django.core import validators
from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class UserModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = CountryField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30, validators=[validators.MinLengthValidator(5, 'It should contain at least 5 characters'), validators.RegexValidator(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W)')])
    
class CategoryModel(models.Model):
    category_name = models.CharField(max_length=100)
    
class BlogModel(models.Model):
    TYPE_BLOG_CHOICES =[
    ('VD', 'Video Blog'),
    ('TX', 'Text Blog'),
    ('AU', 'Podcast Blog'),
    ('VR', 'Virtual Blog'),
    ('OT', 'Other Blog'),   
]
    id = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=512)
    subtitle = models.TextField()
    liked_by = models.UUIDField(unique=True, editable=False)
    type_blog = models.CharField(max_length=2, choices=TYPE_BLOG_CHOICES)
    background = models.ImageField()
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    category = models.OneToOneField(CategoryModel, on_delete=models.CASCADE) 
    
   
class CommentModel(models.Model):
    user = models.UUIDField(editable=False)
    comment = models.TextField()
    time = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    
class BlogSectionsModel(models.Model):
    TYPE_BLOG_SECTIONS_CHOICES = [
        ('1','total'),
        ('2','2:1'),
        ('3','1:2'),
        ('4','1:1:1'),
    ]
    type = models.CharField(max_length=1, choices=TYPE_BLOG_SECTIONS_CHOICES)
    content = models.TextField()
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)

class BlogSectionImagesModel(models.Model):
    image = models.ImageField()
    blog_section = models.ForeignKey(BlogSectionsModel, on_delete=models.CASCADE)

    
    
    
    

    
    
    