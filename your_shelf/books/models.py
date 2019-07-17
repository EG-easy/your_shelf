from django.db import models
from django.urls import reverse
# Create your models here.

class Book(models.Model):
    """本モデル"""
    class Meta:
        # テーブル名を定義
        db_table = 'book'
        app_label= 'books'

    ATTRS_CHOICE = [
        ('Data Science', 'Data Science'),
        ('Web', 'Web'),
        ('Mobile', 'Mobile'),
        ('Cloud', 'Cloud'),
        ('起業', '起業'),
        ('その他', 'その他')
    ]

    # フィールドを定義
    # attrs = models.ChoiceField(verbose_name='Categories', null=True, blank=True, max_length=3, choices=ATTRS_CHOICES)
    attrs = models.CharField(verbose_name='Tag', null=True, blank=True, max_length=12, choices=ATTRS_CHOICE, default='Data Science')
    owner = models.CharField(verbose_name='Owner', max_length=255)
    borrower = models.CharField(verbose_name='Borrower', null=True, blank=True, max_length=255)
    title = models.CharField(verbose_name='Tile', max_length=255, primary_key=True)
    isbn = models.IntegerField(verbose_name='ISBN', null=True, blank=True)
    image = models.ImageField(verbose_name='Image', null=True, blank=True, upload_to='images/books/')
    author = models.CharField(verbose_name='Author', max_length=255, null=True, blank=True)
    price = models.IntegerField(verbose_name='Price', null=True, blank=True)
    publisher = models.CharField(verbose_name='Publisher', max_length=255, null=True, blank=True)
    publish_date = models.DateField(verbose_name='Publish Date', null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)

    def __str__(self):
        # 管理画面などで表示するstrにtitleを設定
        return self.title

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'title': self.title})
