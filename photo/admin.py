from django.contrib import admin

# Register your models here.
from .models import Category, PhotoPost

class CategoryAdmin(admin.ModelAdmin):
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

class PhotoPostAdmin(admin.ModelAdmin):
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

# Django管理サイトにCategory,CategoryAdminを登録する
admin.site.register(Category, CategoryAdmin)
# Django管理サイトにPhotoPost,PhotoPostAdminを登録する
admin.site.register(PhotoPost, PhotoPostAdmin)