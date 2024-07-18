from django.shortcuts import render , redirect
from .forms import AuthorsForm
from .models import Author
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

def index(request):
    authors = Author.objects.all()
    return render(request, 'index.html.django', {'authors': authors})


def detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'detail.html.django', {'author': author})

def add(request):
    if request.method == 'POST':
        form = AuthorsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorsForm()
    return render(request, 'add.html.django', {'form': form})

def edit(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == 'POST':
        form = AuthorsForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorsForm(instance=author)
    return render(request, 'edit.html.django', {'form': form})

def delete(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('home')
    else:
        return render(request, 'delete.html.django', {'author': author})


class AddAuthorView(CreateView):
    model = Author
    form_class = AuthorsForm
    template_name = 'index.html.django'
    success_url = reverse_lazy('home')
def add(request):
    if request.method == 'POST':
        form = AuthorsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorsForm()
    return render(request, 'add.html.django', {'form': form})

