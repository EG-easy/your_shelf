from django.db import models
from django.urls import reverse
# Create your models here.

class Book(models.Model):
    """本モデル"""
    class Meta:
        # テーブル名を定義
        db_table = 'book'
        app_label= 'books'

    # フィールドを定義
    owner = models.CharField(verbose_name='Owner', max_length=255)
    borrower = models.CharField(verbose_name='Borrower', null=True, blank=True, max_length=255)
    title = models.CharField(verbose_name='タイトル', max_length=255, primary_key=True)
    isbn = models.IntegerField(verbose_name='ISBN', null=True, blank=True)
    image = models.ImageField(verbose_name='画像', null=True, blank=True, upload_to='images/books/')
    author = models.CharField(verbose_name='著者', max_length=255, null=True, blank=True)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    publisher = models.CharField(verbose_name='出版社', max_length=255, null=True, blank=True)
    publish_date = models.DateField(verbose_name='出版日', null=True, blank=True)
    description = models.TextField(verbose_name='説明', null=True, blank=True)

    def __str__(self):
        # 管理画面などで表示するstrにtitleを設定
        return self.title

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'title': self.title})
