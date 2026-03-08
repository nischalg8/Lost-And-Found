from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Item
from .forms import ItemForm

@login_required
def list_items(request):
    items = Item.objects.all().order_by('-date_found')
    
    filter_type = request.GET.get('type')
    if filter_type == 'lost':
        items = items.filter(post_type='lost')
    elif filter_type == 'found':
        items = items.filter(post_type='found')
    elif filter_type == 'my':
        items = items.filter(found_by=request.user)
    
    return render(request, 'items/list.html', {'items': items, 'filter_type': filter_type})

@login_required
def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            item = form.save(commit=False)
            item.found_by = request.user
            item.save()
            return redirect("items:list_items")
    else:
        form = ItemForm(user=request.user)
        form.fields.pop('status', None)  # New posts always start as 'not_claimed'
    
    return render(request, "items/item_form.html", {"form": form})

@login_required
def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item.found_by != request.user:
        return HttpResponseForbidden("You are not allowed to edit this item.")
    
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("items:detail_item", pk=item.pk)
    else:
        form = ItemForm(instance=item, user=request.user)

    return render(request, 'items/item_form.html', {'form': form})

@login_required
def detail_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'items/details.html', {'item': item})

@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item.found_by != request.user:
        return HttpResponseForbidden("You cannot delete this item.")
    item.delete()
    return redirect("items:list_items")