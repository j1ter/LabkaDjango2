from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError

from django.shortcuts import render, redirect

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

def categories(request, cat):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def permission_denied(request, exception):
    return HttpResponseForbidden('<h1>Доступ запрещён</h1>')

def bad_request(request, exception):
    return HttpResponseBadRequest('<h1>Невозможно обработать запрос</h1>')

def server_error(request):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>')

