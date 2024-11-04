from django.core.paginator import Paginator,EmptyPage
from django.shortcuts import render,redirect,get_object_or_404
from library import views
from .forms import AuthorForm,BookForm
from .models import Book

# Create your views here.
def author(request):
    if request.method=="POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list')
    else:
        form = AuthorForm()
    return render(request,'author.html',{'form':form})


def book_add(request):
    if request.method=="POST":
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/list')
    else:
        form = BookForm()
    return render(request,'book_add.html',{'form':form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    print(book)
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES,instance=book)  # Support file uploads
        if form.is_valid():
            form.save()
        return redirect('/list')  
    else:
        form = BookForm(instance=book)
    return render(request, 'book_update.html', {'form': form})


def list(request):
    books = Book.objects.all().order_by("title")
    paginator = Paginator(books,5)
    page_number = request.GET.get('page')
    print(page_number)
    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(page_number.num_page)
    print(page)
    return render(request,'list.html',{'books':books,'page':page})

def book_delete(request, pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method=='POST':
            book.delete()
            return redirect('book_list')
    return render(request,'book_delete.html',{'book':book})


def book_details(request,pk):
    book = get_object_or_404(Book,pk=pk)
    books = Book.objects.get(id=pk)
    print("books",books)
    return render(request,'book_details.html',{'books':books})
        





