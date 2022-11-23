from django.shortcuts import render
from django.views import generic

from .models import Page, PageImages


# Create your views here.
def index(request):
    return render(request, '../templates/index.html')

class PageListView(generic.ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        return context

class PageView(generic.DetailView):
    model = Page
    template_name = 'pages/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_images'] = PageImages.objects.filter(page=self.object)
        return context