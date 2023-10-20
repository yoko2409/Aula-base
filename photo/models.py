from django.db import models

# Create your models here.
from accounts.models import CustomUser

class Category(models.Model):
    title = models.CharField(
        # フィールドのタイトル
        verbose_name='カテゴリ',
        max_length=20)

    def __str__(self):
        # オブジェクトを文字列に変換して返す
        return self.title

class PhotoPost(models.Model):
    # CustomUserモデルとPhotoPostモデルを1対多の関係で結びつける
    objects = None
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='ユーザー',
        # ユーザーを削除する場合はそのユーザーの投稿データも全て削除する
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        # フィールドのタイトル
        verbose_name='カテゴリ',
        # カテゴリに関連づけられた投稿データが存在する場合はそのカテゴリを削除できないようにする
        on_delete=models.PROTECT
    )
    # タイトル用のフィールド
    title = models.CharField(
        # フィールドのタイトル
        verbose_name='タイトル',
        max_length=200
    )
    # コメント用のフィールド
    comment = models.TextField(
        verbose_name='コメント',
    )
    # イメージのフィールド1
    image1 = models.ImageField(
        # フィールドのタイトル
        verbose_name='イメージ1',
        # MEDIA_ROOT以下のphotosにファイルを保存
        upload_to='photos'
    )
    # イメージのフィールド2
    image2 = models.ImageField(
        # フィールドのタイトル
        verbose_name='イメージ2',
        # MEDIA_ROOT以下のphotosにファイルを保存
        upload_to='photos',
        # フィールド値の設定は必須でない
        blank=True,
        # データベースにnullが保存されることを許容
        null=True
    )
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        # フィールドのタイトル
        verbose_name='投稿日時',
        # 日時を自動追加
        auto_now_add=True
    )

    def __str__(self):
        return self.title

class Material(models.Model):
    # フィールドのタイトル
    title = models.CharField(max_length=200)
    # 記事内容のフィールド
    content = models.TextField(blank=True)
    # アップロードファイルのフィールド
    file = models.FileField(upload_to='materials/', blank=True, null=True)
    # クラス名のフィールド
    class_name = models.ForeignKey(
        PhotoPost,
        on_delete=models.CASCADE)
    # 作成ユーザーのフィールド
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='ユーザー',
        # ユーザーを削除する場合はそのユーザーの投稿データも全て削除する
        on_delete=models.CASCADE
    )
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        # フィールドのタイトル
        verbose_name='投稿日時',
        # 日時を自動追加
        auto_now_add=True)
