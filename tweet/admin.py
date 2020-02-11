from django.contrib import admin
from tweet.models import Tweet, User


# admin.site.register(Tweet)
# admin.site.register(User)


class UserInstanceInline(admin.TabularInline):
    model = User


class TweetInstanceInline(admin.TabularInline):
    model = Tweet


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'password', 'created_at', 'updated_at')

    # inlines = [TweetInstanceInline]
    ordering = ('id', 'email')
    search_fields = ('email', 'created_at')

    fields = ['email', 'password', ('created_at', 'updated_at')]


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_filter = ('created_at', 'updated_at', 'is_retweet')
    # inlines = [UserInstanceInline]

    fieldsets = (
        ('Detail',  {
            'fields': ('body', 'is_retweet')
        }),
        ('Author', {
            'fields': ('author', 'owner')
        }),
        ('Date', {
            'fields': ('created_at', 'updated_at')
        }),
    )
