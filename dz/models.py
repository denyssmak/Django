from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Article(models.Model):
	name_articles = models.CharField(max_length=30, default='name')
	text = models.TextField(default='text')
	author_articles = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles_author')
	myarticle_like = models.ManyToManyField(User, related_name='my_like_articles', null=True, blank=True)
	myarticle_dislike = models.ManyToManyField(User, related_name='dislike_articles', null=True, blank=True)
	myarticle_create = models.DateTimeField(default=timezone.now)
	myarticle_update = models.DateTimeField(auto_now=True) 

	def __str__(self):
		return f'{self.name_articles} | author: {self.author_articles} | {self.myarticle_like.count() - self.myarticle_dislike.count()} likes | {self.myarticle_create} | {Comment.objects.filter(comment_article__name_articles=self.name_articles).count()} commets'

class Comment(models.Model):
	comment_article = models.ForeignKey(Article, on_delete=models.CASCADE)
	text = models.TextField(default='text')
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_author_comments')
	comment_like = models.ManyToManyField(User, related_name='pub_like_comments', null=True, blank=True)
	comment_dislike = models.ManyToManyField(User, related_name='dislike_user_articles', null=True, blank=True)
	comment_create = models.DateTimeField(default=timezone.now)
	comment_update = models.DateTimeField(auto_now=True)
	comment = models.ForeignKey('dz.Comment', null=True, blank=True, on_delete=models.CASCADE, related_name='comments')

	def __str__(self):
		return f'author commets: {self.author} | {self.comment_like.count() - self.comment_dislike.count()} likes | {self.comment_create}'


