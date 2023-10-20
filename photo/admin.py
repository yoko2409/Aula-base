from django.contrib import admin

# Register your models here.
from .models import Category, PhotoPost, Material

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

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'class_name', 'user', 'content', 'posted_at')
    list_display_links = ('id', 'title', 'class_name', 'user', 'content', 'posted_at')

# Django管理サイトにCategory,CategoryAdminを登録する
admin.site.register(Category, CategoryAdmin)
# Django管理サイトにPhotoPost,PhotoPostAdminを登録する
admin.site.register(PhotoPost, PhotoPostAdmin)
# Django管理サイトにMaterial,MaterialAdminを登録する
admin.site.register(Material, MaterialAdmin)