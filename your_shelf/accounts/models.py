from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    class Meta:
        db_table = 'custom_user'
        app_label = 'accounts'

    INTEREST_CHOICE = [
        ('Data Science', 'Data Science'),
        ('Web', 'Web'),
        ('Mobile', 'Mobile'),
        ('Cloud', 'Cloud'),
        ('起業', '起業'),
        ('その他', 'その他')
    ]

    # フィールドを定義
    name = models.CharField(verbose_name='Name', max_length=255, primary_key=True)
    photo = models.ImageField(verbose_name='Photo', null=True, blank=True, upload_to='images/accounts/')
    email = models.EmailField(verbose_name='E-mail', blank=True)
    password = models.CharField(verbose_name='Password', max_length=128)
    interest = models.CharField(verbose_name='Interest', null=True, blank=True, max_length=12, choices=INTEREST_CHOICE, default='Data Science')

    def __str__(self):
        # 管理画面などで表示するstrにtitleを設定
        return self.name
