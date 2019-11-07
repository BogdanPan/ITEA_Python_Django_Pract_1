from django.shortcuts import render
from .models import Post, Comment
from django.db.models import Count


def article(request, article_slug):
	post = Post.find_by_slug(article_slug)
	comments = Comment.find_by_art(post)
	if post:
		ctx = {'post': post, 'comments': comments}
		return render(request, 'core/post.html', ctx)
	else:
		return render(request, 'core/error404.html')


def index(request):
	query = Post.objects.all().order_by('-created')
	ctx = {'posts': query, 'number_of_posts': len(query)}

	return render(request, 'core/main_page.html', ctx)


def articles(request):
	ctx = {'posts': Post.objects.all()}
	return render(request, 'core/posts.html', ctx)
