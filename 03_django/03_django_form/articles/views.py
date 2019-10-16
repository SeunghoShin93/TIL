from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import Http404
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
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
    comments = article.comment_set.all()
    commentform = CommentForm() # 댓글 폼
    context = {'article':article, 'commentform':commentform, 'comments':comments}
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')

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

@require_POST

def comments_create(request, article_pk):
    commentform = CommentForm(request.POST)
    if commentform.is_valid():
        # 객체 생성 하지만 DB에 레코드는 작성하지 않는다.
        comment = commentform.save(commit=False)
        comment.article_id = article_pk
        comment.save()
    return redirect('articles:detail', article_pk)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()

        # return redirect('articles:detail' article.pk)
        # return redirect('articles:detail' article_pk)

    return redirect('article:detail', article_pk)
