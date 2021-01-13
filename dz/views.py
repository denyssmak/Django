from django.http import HttpResponse

def index(request):
	return HttpResponse('index')

def articles(request):
	return HttpResponse('articles')

def article(request):
	return HttpResponse('article')

def users(request):
	return HttpResponse('users')

def articles_arhive(request):
	return HttpResponse('articles_arhive')

def article_num(request, article_number):
	return HttpResponse(article_number)

def article_num_arhive(request, article_number):
	return HttpResponse('{} arhive'.format(article_number))

def article_num_slug(request, article_number, slug_text):
	return HttpResponse('{} {}'.format(article_number, slug_text))

def users_num(request, user_number):
	return HttpResponse('{} - user'.format(user_number))

