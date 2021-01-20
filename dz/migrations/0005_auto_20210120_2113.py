# Generated by Django 3.1.5 on 2021-01-20 19:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dz', '0004_auto_20210120_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='myarticle_dislike',
            field=models.ManyToManyField(blank=True, null=True, related_name='dislike_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='myarticle_like',
            field=models.ManyToManyField(blank=True, null=True, related_name='my_like_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_dislike',
            field=models.ManyToManyField(blank=True, null=True, related_name='dislike_user_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_like',
            field=models.ManyToManyField(blank=True, null=True, related_name='pub_like_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]