from django.contrib import admin
from .models import Education, Experience, Project, Blog, ContactMessage, Certificate


# ─── Site Branding ───────────────────────────────────────────────────────
admin.site.site_title = "Abhay's Portfolio"
admin.site.site_header = "Abhay's Portfolio — Admin"
admin.site.index_title = "Manage Your Content"


# ─── Education ───────────────────────────────────────────────────────────
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'duration', 'order')
    list_editable = ('order',)
    search_fields = ('institution', 'degree')
    ordering = ('order',)


# ─── Experience ──────────────────────────────────────────────────────────
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('organization', 'role', 'duration', 'partner_label', 'order')
    list_editable = ('order',)
    search_fields = ('organization', 'role')
    ordering = ('order',)


# ─── Project ─────────────────────────────────────────────────────────────
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'github_link', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'tech_stack')
    ordering = ('order',)


# ─── Blog ────────────────────────────────────────────────────────────────
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('title', 'content')
    ordering = ('-created_at',)


# ─── Contact Messages (Read-only) ───────────────────────────────────────
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'short_message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)
    readonly_fields = ('name', 'email', 'message', 'created_at')

    def short_message(self, obj):
        return obj.message[:80] + '...' if len(obj.message) > 80 else obj.message
    short_message.short_description = 'Message'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


# ─── Certificates ────────────────────────────────────────────────────────
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'status', 'order')
    list_editable = ('order',)
    list_filter = ('issuer', 'status')
    search_fields = ('title', 'issuer', 'topics')
    ordering = ('order',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'issuer', 'topics')
        }),
        ('Media & Links', {
            'fields': ('image', 'icon', 'certificate_link')
        }),
        ('Status Tracking', {
            'fields': ('status', 'order')
        }),
    )