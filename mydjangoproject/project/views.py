from django.shortcuts import render, redirect, get_object_or_404
from .forms import TagForm, QuoteForm, AuthorForm
from .models import Tag, Quotes, Authors

# Create your views here.
def main(request):
    quotes = Quotes.objects.all()
    return render(request, 'project/index.html', {"quotes": quotes})


def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='project:main')
        else:
            return render(request, 'project/tag.html', {'form': form})

    return render(request, 'project/tag.html', {'form': TagForm()})


def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='project:main')
        else:
            return render(request, 'project/author.html', {'form': form})

    return render(request, 'project/author.html', {'form': AuthorForm()})


def quote(request):
    tags = Tag.objects.all()

    if request.method == "POST":
        form = QuoteForm(request.POST)

        if form.is_valid():
            quote = form.save()
            author_name = form.cleaned_data["author"]
            author = get_object_or_404(Authors, fullname=author_name)
            quote.author = author
            quote.save()
            chosen_tags = form.cleaned_data["tags"]
            quote.tags.set(chosen_tags)
            return redirect(to="project:main")
        
        else:
            return render(request, "project/quote.html", {"tags": tags, "form": form})
        
    return render(request, "project/quote.html", {"tags": tags, "form": QuoteForm()})


def quote_info(request, quote_id):
    quote = get_object_or_404(Quotes, pk=quote_id)
    return render (request, 'project/quote_detail.html', {'quote': quote})


def about_author(request, author_name):
    author = get_object_or_404(Authors, fullname=author_name)
    return render(request, "project/author_detail.html", {"author": author})