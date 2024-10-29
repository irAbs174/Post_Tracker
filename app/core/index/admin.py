from .tracker_models import ScreenShot
from django.contrib import admin

@admin.register(ScreenShot)
class ScreenShotAdmin(admin.ModelAdmin):
    list_display = ('orders_number', 'tracking_number', 'phone_number', 'customer', 'created_at', 'updated_at')
    search_fields = ('orders_number', 'customer', 'tracking_number')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    # Optional: Customize the form layout in the admin
    fieldsets = (
        (None, {
            'fields': ('orders_number', 'tracking_number', 'phone_number', 'customer', 'image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('created_at', 'updated_at')
