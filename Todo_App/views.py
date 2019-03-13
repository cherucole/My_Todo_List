from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *


def homepage(request):
    items = Item.objects.all()
    number = len(items)
    context = {
        'list_items': items,
        'name': 'cherucole',
        'length': number  # if something is referenced above do not put it in quotes because it already has a value so just use name
    }
    # items = Item.objects.all()
    return render(request, 'index.html', context)


def item(request, id):
    item = Item.objects.get(id=id)
    context = {
        'list_item': item,
        'name': 'cherucole'
    }
    return render(request, 'details.html', context)


def item_delete(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'index.html', {'list_item': item})


def todo_delete(request, id):
    item = get_object_or_404(Item, id=id)  # Get your current item
    if request.method == 'POST':         # If method is POST,
        item.delete()                     # delete the item.
        return redirect('/')             # Finally, redirect to the homepage.
    return render(request, 'details.html', {'list_item': item})
    # If method is not POST, render the default template.


def add_item(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        body = request.POST['body']

        item = Item(title=title, body=body)
        item.save()

        return redirect('items:homepage')

    else:
        return render(request, 'add.html')
