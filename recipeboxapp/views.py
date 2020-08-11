from django.shortcuts import render, HttpResponsePermanentRedirect, reverse
from recipeboxapp.models import Author, Article
from recipeboxapp.forms import RecipeForm, AuthorForm


# Create your views here.


def index(request):
    recipes = Article.objects.all()
    author = Author.objects.all()
    return render(request, "index.html", {"recipe": recipes, "author": author})


def recipe_detail(request, post_id):
    recipes = Article.objects.filter(id=author_id).first()
    author = Author.objects.filter(author=author.id)
    return render(request, "user_detail.html", {"author": author, "recipes": recipes})


def recipe_form_view(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Article.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                time_required=data.get('time_required'),
                author=data.get('author'),
                instructions=data.get('instructions')
            )
            return HttpResponsePermanentRedirect(reverse("homepage"))
    form = RecipeForm()
    return render(request, "generic_form.html", {"form": form})


def author_form_view(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponsePermanentRedirect(reverse("homepage"))
    form = AuthorForm()
    return render(request, "generic_form.html", {"form": form})
