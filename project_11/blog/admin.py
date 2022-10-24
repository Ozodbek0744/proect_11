from django.contrib import admin
from .models import BlogModel, Comment, Izoh


# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class BlogModelAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


class IzohInline(admin.TabularInline):
    model = Izoh
    extra = 0


class CommentAdmin(admin.ModelAdmin):
    inlines = [IzohInline]


admin.site.register(Izoh)
admin.site.register(Comment)
admin.site.register(BlogModel, BlogModelAdmin)




