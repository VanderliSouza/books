from django.shortcuts import render
from .models import Book
from django.views import generic

'''
def about(request):
    return render(request, 'books/about.html')
'''

def about(request):
    latest_question_list = Book.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'books/about.html', context)

def book_list(request, posts_id):
    posts = Book.objects.get(pk=posts_id)
    return render(request, 'books/book.html', {'posts': posts})

'''

class DetailView(generic.DetailView):
    template_name = 'books/book.html'
    model = Book
  
    context_object_name = "latest_question_list"

    @property
    def get_queryset(self):
        return Book.objects.order_by('-title')[:5]




def book(request):
    books = Book.objects.all()
    return render(request, 'books/book.html', {"data": books})
'''