from django.contrib import admin
from .models import Activity, ActivityPrice, ActivityImage, ActivitySession, ActivityType

class PriceTableInline(admin.TabularInline):
    model = ActivityPrice.activities.through
    extra = 1

class PriceAdmin(admin.ModelAdmin):
    inlines = (PriceTableInline,)
    exclude = ('activities',)
    list_display = ('price', 'note', 'date_created', 'date_updated')

class ActivityImageInline(admin.TabularInline):
    model = ActivityImage
    extra = 1

class ActivitySessionInline(admin.TabularInline):
    model = ActivitySession
    extra = 1

class ActivityAdmin(admin.ModelAdmin):
    inlines = [ActivityImageInline, ActivitySessionInline, PriceTableInline]
    list_display = ('name', 'date_created', 'date_updated', 'type', 'visibility')
    list_filter = ('date_created', 'date_updated', 'type', 'visibility')
    search_fields = ('name', 'description')
    date_hierarchy = 'date_created'
    ordering = ('-date_created',)

class ActivityTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityType, ActivityTypeAdmin)