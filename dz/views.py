import random

import string

from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
	data = {'random_int': random.randint(1, 100), 'random_slug': ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))}
	return render(request, 'index.html', data)

def articles(request):
	return HttpResponse('articles')

def article(request):
	return HttpResponse('article')

def users(request):
	return HttpResponse('users')

def articles_arhive(request):
	return HttpResponse('articles_arhive')

def article_num(request, article_number):
	data = {'article_num': article_number}
	return render(request, 'id.html', data)

def article_num_arhive(request, article_number):
	return HttpResponse('{} arhive'.format(article_number))

def article_num_slug(request, article_number, slug_text):
	data = {'article_num': article_number, 'slug': slug_text,}
	return render(request, 'id.html', data)

def users_num(request, user_number):
	return HttpResponse('{} - user'.format(user_number))

