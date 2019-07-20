# Generated by Django 2.2.2 on 2019-07-20 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='interest',
            field=models.CharField(blank=True, choices=[('Data Science', 'Data Science'), ('Web', 'Web'), ('Mobile', 'Mobile'), ('Cloud', 'Cloud'), ('起業', '起業'), ('その他', 'その他')], default='Data Science', max_length=12, null=True, verbose_name='Interest'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/accounts/', verbose_name='Photo'),
        ),
    ]
