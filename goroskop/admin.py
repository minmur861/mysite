from django.contrib import admin
from goroskop.models import UserProfile, Sex, Country, Zodiac, Age


class ProfileAdmin(admin.ModelAdmin):
    fieds = ('user', 'avatar')
    list_display = ('avatar',)


admin.site.register(UserProfile)
admin.site.register(Sex)
admin.site.register(Country)
admin.site.register(Zodiac)
admin.site.register(Age)
