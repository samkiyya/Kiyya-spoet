from django.contrib import admin
from .models import Poet, Quote, Video, Contact, Blog

# Register your models here.

class PoetAdmin(admin.ModelAdmin):
    readonly_fields = ()

class QuoteAdmin(admin.ModelAdmin):
    readonly_fields = ()

class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ()

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ()


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Poet, PoetAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Blog, BlogAdmin)
