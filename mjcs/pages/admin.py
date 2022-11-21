from django.contrib import admin
from .models import Page, PageCategory, PageImages, MainPage


class PageCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'menu_visibility', 'main_color')
    search_fields = ('name', 'description')
    ordering = ('order',)

class ImageAdmin(admin.TabularInline):
    model = PageImages
    extra = 1

class PageAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'created', 'updated', 'category', 'visibility', 'order', 'slug')
    list_filter = ('created', 'updated', 'category', 'visibility')
    search_fields = ('title', 'content')
    date_hierarchy = 'created'
    ordering = ('-created',)

class MainPageAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'created', 'updated')
    list_filter = ('created', 'updated')
    exclude = ('category', 'visibility')

admin.site.register(Page, PageAdmin)
admin.site.register(PageCategory, PageCategoryAdmin)
admin.site.register(MainPage)


