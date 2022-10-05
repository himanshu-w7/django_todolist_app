from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todolist, Categories


def index(request):
    todos = Todolist.objects.all().values()
    categories = Categories.objects.all()

    if request.method == "POST":

        try:
            if 'taskadd' in request.POST:
                title = request.POST['description']
                date = str(request.POST['date'])
                category = request.POST['select_category']
                content = title + '---' + category + '---' + date
                todo = Todolist(title=title, due_date=date, category=Categories.objects.get(name=category),
                                content=content)
                todo.save()
        except:
            params = {'todos': todos, 'categories': categories, 'error': "data is not valid"}
            return render(request, 'index.html', params)
        try:

            if 'taskdelete' in request.POST:
                checked_item = request.POST['checkbox']
                todo = Todolist.objects.get(id=checked_item)
                todo.delete()
        except:
            params = {'todos': todos, 'categories': categories, 'error': "Uncheck not Allowed"}
            return render(request, 'index.html', params)
    params = {'todos': todos, 'categories': categories}
    return render(request, 'index.html', params)
