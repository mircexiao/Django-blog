from django.contrib import admin
from .models import UserProfile
from .models import UserInfo

class UserProfiileAdmin(admin.ModelAdmin):
    list_display = ('user','birth','phone')
    list_filter = ("phone",)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user","school","company","profession","address","about_me","profession")
    list_filter = ("school","company","profession")

admin.site.register(UserProfile,UserProfiileAdmin)
admin.site.register(UserInfo,UserInfoAdmin)