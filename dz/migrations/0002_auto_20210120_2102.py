# Generated by Django 3.1.5 on 2021-01-20 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author_articles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='myarticle_create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='article',
            name='myarticle_dislike',
            field=models.ManyToManyField(related_name='dislike_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='myarticle_like',
            field=models.ManyToManyField(related_name='my_like_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='myarticle_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='article',
            name='name_articles',
            field=models.CharField(default='name', max_length=30),
        ),
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(default='text'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_create', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment_update', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(default='default title', on_delete=django.db.models.deletion.CASCADE, related_name='_myauthor_comments', to=settings.AUTH_USER_MODEL)),
                ('comment_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dz.article')),
                ('comment_dislike', models.ManyToManyField(related_name='dislike_user_articles', to=settings.AUTH_USER_MODEL)),
                ('comment_like', models.ManyToManyField(related_name='pub_like_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
