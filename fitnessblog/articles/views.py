from django.shortcuts import render, redirect
from .models import Article, Comment
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from . import forms


def article_list(request):
    articles = Article.objects.all().order_by("date")
    return render(request, "articles/article_list.html", {'articles': articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    commentform = forms.CreateComment
    return render(request, 'articles/article_detail.html', {'article': article, 'commentform': commentform})


@login_required()
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to database
            instance = form.save(commit=False)
            # set the author field to the loggged in user
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})


class AddCommentView(CreateView):
    model = Comment
    template_name = 'articles/add_comment.html'
    fields = '__all__'
