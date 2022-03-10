from django.contrib import admin
from .models import Post, Category,Contact, BlogComment, IpModel, SubcribeUsers,CustomUserAdmin,  ReplayComment
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_title',)
    icon_name = 'apps'

# class CommentAdmin(admin.ModelAdmin):
#     list_display =('post','username')
class ContactAdmin(admin.ModelAdmin):
    list_display=("fname","email","phone")
    icon_name='contact_phone'

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','post_date',)
    search_fields = ('tags',)
    list_filter= ('category',)
    list_per_page = 10
    icon_name='add_to_photos'

class SubAdmin(admin.ModelAdmin):
    icon_name='verified_user'
    list_display=('email','date')

class blgAdmin(admin.ModelAdmin):
    icon_name='message'
    list_display=('user','timestamp')
class customadmin(admin.ModelAdmin):
    icon_name='person'
    list_display=('user','phone')

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(BlogComment,blgAdmin)
admin.site.register(IpModel)
# admin.site.register(ReplayComment)
admin.site.register(CustomUserAdmin,customadmin)
