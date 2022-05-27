from django.contrib import admin
from blog_app.models import (
    BlogsModel,
    BlogSectionImagesModel,
    BlogSectionsModel,
    CategoriesModel,
    CommentsModel,
    # UsersModel,
)

# Register your models here.


admin.site.register(BlogsModel)
admin.site.register(BlogSectionImagesModel)
admin.site.register(BlogSectionsModel)
admin.site.register(CategoriesModel)
admin.site.register(CommentsModel)
# admin.site.register(UsersModel)
