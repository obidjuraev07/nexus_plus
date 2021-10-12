from django.contrib import admin
from .models import Blog, Comments
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    exclude = ['slug']


class CommentsAdmin(admin.ModelAdmin):
    formfield_overrides = {

        models.TextField: {'widget': TinyMCE()}

    }


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comments, CommentsAdmin)
