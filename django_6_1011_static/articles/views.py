from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# view 함수가 특정한 요청 method만 허용하도록 하는 데코레이터
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# create
# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'articles/new.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # article = form.save()
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            # 유효성 검사 통과하면 상세 페이지로 리다이렉트
            return redirect('articles:detail', article.pk)
    else: # request.method == 'GET' -> new와 create 합침
        form = ArticleForm()
    # # 통과하지 못하면 작성 페이지로 리다이렉트
    # print(f'에러: {form.errors}')
    context = {
        'form': form,
    }
    # return render(request, 'articles/new.html', context)
    return render(request, 'articles/create.html', context)
    # return redirect('articles:new')

    # article = Article(title=title, content=content)
    # article.save()

    # return render(request, 'articles/create.html')
    # return render(request, 'articles/index.html') # index로 갔을 때 게시물이 보이지 않음
    # return redirect('articles:index') # 불필요해진 create 삭제
    # return redirect('articles:detail', article.pk)

@require_safe
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

# delete
# @login_required
@require_POST
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user.is_authenticated:
        # if request.method == 'POST':
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)

# update
# def edit(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user:
        # edit, update 합치기
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            # article.title = request.POST.get('title')
            # article.content = request.POST.get('content')
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
            # return redirect('articles:detail', article.pk)
        # article.save()
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)

@require_POST
def comments_create(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)