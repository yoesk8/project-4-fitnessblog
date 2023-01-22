from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from .models import Article, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from . import forms


def article_list(request):
    articles = Article.objects.all().order_by("date")
    return render(request, "articles/article_list.html", {'articles': articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    total_likes = article.total_likes()
# In order to pass the liked to the frontend set it to false if the user has liked this article already
    liked = False
    if article.likes.filter(id=request.user.id).exists():
        liked = True
    return render(request, 'articles/article_detail.html', {'article': article,
                                                            'total_likes': total_likes,
                                                            'liked': liked})


@login_required()
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article but don't commit to database
            instance = form.save(commit=False)
            # set the author field to the loggged in user
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})


def LikeView(request, slug):
    post = get_object_or_404(Article, id=request.POST.get('article_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('articles:detail', args=[str(slug)]))


class AddCommentView(CreateView):
    model = Comment
    template_name = 'articles/add_comment.html'
    form_class = forms.CommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.article_slug = self.kwargs['slug']
        article = Article.objects.get(slug=self.kwargs['slug'])
        form.instance.post_id = article.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('articles:detail', kwargs={'slug': self.kwargs['slug']})


class UpdateArticleView(UpdateView):
    model = Article
    template_name = 'articles/article_edit.html'
    fields = ['title', 'body', 'thumb', 'category']

    def get_success_url(self):
        return reverse_lazy('articles:detail', kwargs={'slug': self.kwargs['slug']})