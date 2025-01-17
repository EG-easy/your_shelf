# Generated by Django 2.1.7 on 2019-07-09 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='user',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='borrower',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Borrower'),
        ),
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.CharField(default='nakai', max_length=255, verbose_name='Owner'),
            preserve_default=False,
        ),
    ]
