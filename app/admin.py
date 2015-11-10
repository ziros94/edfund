from django.contrib import admin
from .models import User, School, Fund, Donation, Club, Incentive, UserProfile
# Register your models here.


class ClubInline(admin.StackedInline):
    model = Club
    extra = 3


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class FundInline(admin.StackedInline):
    model = Fund
    extra = 3


class SchoolAdmin(admin.ModelAdmin):
    inlines = [ClubInline]


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
    inlines = [UserProfileInline, ClubInline]


class ClubAdmin(admin.ModelAdmin):
    inlines = [FundInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Fund)
admin.site.register(Donation)
admin.site.register(Club, ClubAdmin)
admin.site.register(Incentive)