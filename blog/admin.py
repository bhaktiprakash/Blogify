from django.contrib import admin
from blog.models import category,blog
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class blogAdmin(SummernoteModelAdmin):
    list_display = ('title','author','category','date')
    search_fields = ('title',)
    list_filter = ('category',)
    summernote_fields = ('description',)


admin.site.register(category)
admin.site.register(blog,blogAdmin)

