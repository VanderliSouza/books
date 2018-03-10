from django.urls import path

from books import views

#from adiciona import views

urlpatterns = (
    # (r'^$', 'agenda.views.lista'),
    # path('', views.index, name='index'),
    path('', views.about, name='about.html'),
    # path('<int:ItemAgenda_id>/', views.adiciona, name='adiciona'),
    # path('<int:Book_id>/', views.book, name='book.html'),
    path('<int:posts_id>/', views.book_list, name='book.html'),

)