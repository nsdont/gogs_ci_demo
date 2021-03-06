from django.shortcuts import render, redirect

from lists.models import Item


def home_view(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST.get('item_text'))
        return redirect('/')
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
