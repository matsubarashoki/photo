from django.contrib import admin
# CustomeUserをインポート
from .models import Category,PhotoPost

class CategoryAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するcolumnを設定するクラス
    '''
    # レコード一覧にidとtitleを表示
    list_display = ('id','title')
    # 表示するcolumnにリンクを設定
    list_display_links = ('id','title')

class PhotoPostAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するcolumnを設定するクラス
    '''
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するcolumnにリンクを設定
    list_display_links = ('id', 'title')

# Django管理サイトにCategory, CategoryAdminを登録する
admin.site.register(Category, CategoryAdmin)

# Django管理サイトにPhotoPost, PhotoPostAdminを登録する
admin.site.register(PhotoPost, PhotoPostAdmin)
