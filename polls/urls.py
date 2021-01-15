from django.urls import path
from . import views


app_name = 'polls'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:questionId>/detail/', views.detail, name='detail'),
#     path('<int:questionId>/results/', views.results, name='results'),
#     path('<int:questionId>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:pageSize>/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:questionId>/vote/', views.vote, name='vote'),
    path('test/', views.TestView.as_view(), name='test'),
]