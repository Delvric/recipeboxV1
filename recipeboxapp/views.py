from django.shortcuts import render, HttpResponsePermanentRedirect, reverse
from recipeboxapp.models import Author, Article
from recipeboxapp.forms import RecipeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    recipes = Article.objects.all()
    author = Author.objects.all()
    return render(request, "index.html", {"recipe": recipes, "author": author})


def recipe_detail(request, post_id):
    recipes = Article.objects.filter(id=post_id).first()
    return render(request, "user_detail.html", {"author": author, "recipes": recipes})


def user_detail(request, author_id):
    author = Author.objects.filter(id=author_id).first()
    recipes = Recipe.objects.filter(author=author_id.id)
    return render(request, "user_detail.html", {"author": author, "recipes": recipes})


@login_required
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


@login_required
def author_form_view(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponsePermanentRedirect(reverse("homepage"))
    form = AuthorForm()
    return render(request, "generic_form.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponsePermanentRedirect(request.GET.get("next", reverse("homepage")))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponsePermanentRedirect(reverse("homepage"))


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
            Author.objects.create(name=data.get("username"), user=new_user)
            login(request, new_user)
            return HttpResponsePermanentRedirect
        form = SignupForm()
        return render(request, "generic_form.html", {"form": form})
