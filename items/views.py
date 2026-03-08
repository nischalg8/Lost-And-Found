from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Item
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
# Create your views here.


@login_required
def list_items(request):
    items =  Item.objects.all()
    return render(request, 'items/list.html', {'items': items})


@login_required
def detail_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'items/details.html', {'item': item})


@login_required
def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.found_by = request.user
            item.save()
            return redirect("items:list_items")
    else:
        form = ItemForm()

    return render(request, "items/item_form.html", {"form": form})

@login_required
def update_item(request, pk):

    item = get_object_or_404(Item, pk=pk)
    
    if item.found_by != request.user:
        return HttpResponseForbidden("You are not allowed to edit this item.")

    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("items:detail_item", pk=item.pk)

    
    return render(request, 'items/item_form.html', {'form': form})

@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if item.found_by != request.user:
        return HttpResponseForbidden("You cannot delete this item.")

    item.delete()
    return redirect("items:list_items")