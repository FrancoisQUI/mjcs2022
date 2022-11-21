from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('page/<slug:slug>/', views.PageView.as_view(), name='page'),
]