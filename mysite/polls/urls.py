from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView, name='index'),

    path('specifics/<int:pk>', views.DetailView, name='detail'),

    path('<int:pk>/results/', views.ResultsView, name='results'),

    # path('', views.index, name='index'),
    #
    # path('specifics/<int:question_id>', views.detail, name='detail'),
    #
    # path('<int:question_id>/results/', views.results, name='results'),

    path('<int:question_id>/vote/', views.vote, name='vote'),
]
