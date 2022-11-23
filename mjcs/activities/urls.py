from django.urls import path
from . import views

app_name = 'activities'
urlpatterns = [
    path('list', views.ActivityListView.as_view(), name='activity_list'),
    path('<slug:slug>/', views.ActivityDetailView.as_view(), name='activity_detail'),
]
