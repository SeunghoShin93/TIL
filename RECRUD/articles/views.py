from django.shortcuts import render, redirect, get_object_or_404

from .forms import ArticleForm, CommentForm

from .models import Article, Comment

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')  
    else:
        form = ArticleForm()
    context = {'form':form}
    return render(request, 'articles/form.html', context)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm(instance=article)
    context = {'form':form}
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {'article':article, 'comments': comments, 'comment_form':comment_form,}
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        article.delete()
    return redirect('articles:index')

def comment_create(request, article_pk):
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article_id = article_pk
            comment.save()
    # context = {'commentform':commentform} 
    return redirect('articles:detail', article_pk)

def comment_delete(request, article_pk, comment_pk):
    if request.method == "POST":
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)

def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')