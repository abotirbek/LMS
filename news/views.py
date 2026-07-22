from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .forms import NewsForm


def get_news(request):
    news = News.objects.all()
    return render(request, 'news/news/news_list.html', {'news': news})


def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/news/create_news.html', {'form': form})


def read_news(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'news/news/read_news.html', {'news': news_item})


def update_news(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news_item)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm(instance=news_item)
    return render(request, 'news/news/update_news.html', {'form': form})


def delete_news(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news_item.delete()
        return redirect('news_list')
    return render(request, 'news/news/delete_news.html', {'news': news_item})
