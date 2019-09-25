from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import Http404
from .models import Article, Comment
from .forms import ArticleForm
from IPython import embed
# Create your views here.



def index(request):
    articles = Article.objects.all()
    #articles = get_list_or_404(Article) 글 개수가 0 이면 에러 나기 때문에 부적절
    context = {'articles':articles}
    return render(request, 'articles/index.html', context)


def create(request):

    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에의한 데이터를 인자로 받는다. 이작접을 binding 작업
        # 이 처리 과정은  BINDING 이라고 불리며 유효성 체크를 할 수 있게 해준다.
        form = ArticleForm(request.POST)

        # FORM 이 유효한지 체크
        if form.is_valid():
            # form.cleaned data 로 정제된 테외터를 받는ㄴ아==
            article = form.save()
            return redirect(article)
    else:
        form = ArticleForm()

    # 상황에 따라 context에 넘어가는 두가지 form
    # 1. get  방식 기본 form
    # 2. post: 검증에 실패 후의 FORM(is_valid == False)
    context = {'form': form,}
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk) 
    
    context = {'article':article,}
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect(article)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        # ArticleForm 을 초기화 (이전에 DB에 저장된 데이터를 넣어준 상태)
        #  form = ArticleForm(initial={'title':article.title, 'content':article.content})
        # __dict__ : article 객체 데이터를 딕셔너리 자료형으로 변환
        form = ArticleForm(instance=article)
    # 1. POST : 검증에 실패한 form (오류 메세지도 포함된 상태)
    # 2. GET : 초기화 된 form
    context = {'form': form, 'article': article}
    return render(request, 'articles/form.html', context) 


def comments_create(request, article_pk):
    # 댓글을 달 게시글
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        # form 에서 넘어온 댓글 정보
        content = request.POST.get('content')
        # 댓글 생성 및 저장
        comment = Comment(article=article, content=content)
        comment.save()
        return redirect(article)
        # return redirect('articles:detail' article.pk)
        # return redirect('articles:detail' article_pk)
    else:
        return redirect(article)


def comments_delete(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()

        # return redirect('articles:detail' article.pk)
        # return redirect('articles:detail' article_pk)

    return redirect('article:detail', article_pk)
