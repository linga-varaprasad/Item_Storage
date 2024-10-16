from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Item

def item_list(request):
    sort_by = request.GET.get('sort', 'name')
    items = Item.objects.all().order_by(sort_by)
    
    paginator = Paginator(items, 5)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'sort_by': sort_by,
    }
    return render(request, 'catalog/item_list.html', context)