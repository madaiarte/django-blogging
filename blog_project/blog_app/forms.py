from django import forms
from blog_app.models import (
    BlogSectionImagesModel,
    BlogSectionsModel,
    BlogsModel,
    CategoriesModel,
    CommentsModel,
)


class BlogsForm(forms.ModelForm):
    class Meta:
        model = BlogsModel
        fields = (
            "title",
            "subtitle",
            "background",
        )

        widget = {
            "title": forms.TextInput(attrs={"class": "fsl-input"}),
            "subtitle": forms.Textarea(attrs={"class": "fsl-input"}),
            "background": forms.FileInput(attrs={"class": "fsl-load-media"}),
        }


class CommentsForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = ["user", "comment"]

        widget = {
            "user": forms.Select(attrs={"class": "fsl-input fsl-static"}),
            "comment": forms.Textarea(
                attrs={"class": "editable medium-editor-textarea postcontent"}
            ),
        }


class CategoriesForm(forms.ModelForm):
    class Meta:
        models = CategoriesModel
        exclude = ["rating"]
        widget = {
            "type_blog": forms.Select(attrs={"class": "fsl-selector-multiple"}),
        }


class BlogSectionForm(forms.ModelForm):
    class Meta:
        model = BlogSectionsModel
        fields = "__all__"
        widget = {
            "type": forms.Select({"class": "fsl-select"}),
            "content": forms.Textarea(
                attrs={"class": "editable medium-editor-textarea postcontent"}
            ),
        }


class BlogSectionImagesForm(forms.ModelForm):
    class Meta:
        model = BlogSectionImagesModel
        fields = "__all__"
        widget = {
            "image": forms.FileInput(attrs={"class": "fsl-load-media"}),
        }
