# django-blogging

This is a project for multi-user blog. You can add pages and allow comments over them.

## Mockup

This is a mockup about the project on fijma
https://www.figma.com/file/BPuJFwMcdTNeJkXtAdc3ye/Untitled?node-id=0%3A1

# Questions?

1. How can I create custom schemas using django?

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "DATABASE_NAME",
        "OPTIONS": {
            "options": "-c search_path=training" #<<-- This part
```
