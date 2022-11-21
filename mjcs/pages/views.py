from django.shortcuts import render
from django.views import generic

from .models import Page, PageImages


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

class PageView(generic.DetailView):
    model = Page
    template_name = 'pages/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_images'] = PageImages.objects.filter(page=self.object)
        return context