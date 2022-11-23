from .models import Page, PageCategory

def pages(request):
    pages = Page.objects.order_by('order')
    return {'pages': pages}

def pages_categories(request):
    categories = PageCategory.objects.order_by('order')
    return {'categories': categories}

