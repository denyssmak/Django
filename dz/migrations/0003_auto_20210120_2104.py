# Generated by Django 3.1.5 on 2021-01-20 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dz', '0002_auto_20210120_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author_articles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='myarticle_dislike',
            field=models.ManyToManyField(related_name='dislike_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='myarticle_like',
            field=models.ManyToManyField(related_name='my_like_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_author_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_dislike',
            field=models.ManyToManyField(related_name='dislike_user_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_like',
            field=models.ManyToManyField(related_name='pub_like_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]