from django.views.generic import ListView, DetailView

from .models import Activity, ActivityType


class  ActivityListView(ListView):
    model = Activity
    template_name = 'activities/activity_list.html'
    context_object_name = 'activities'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activity_type'] = ActivityType.objects.all()
        return context


class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'activities/activity_detail.html'
    context_object_name = 'activity'
