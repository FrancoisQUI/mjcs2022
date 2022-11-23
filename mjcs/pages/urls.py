from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.PageListView.as_view(), name='page_list'),
    path('<slug:slug>/', views.PageView.as_view(), name='page'),
]