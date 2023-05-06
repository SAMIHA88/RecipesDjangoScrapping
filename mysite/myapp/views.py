from urllib import request

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *
from .forms import *
from .scrapper.scrape import scrape
from .scrapper.import_data import importData
import json
import random


# Create your views here.
def home(request):
    return render(request, 'home.html')


def search(request):
    keyW = request.GET.get('kw')
    recettes = Recette.objects.filter(nom__contains=keyW)
    return render(request, 'recettes.html', {'recettes': recettes})

def list_recette(request):
    """""
    for i in range(10):
        Recette(None,f.titre(),f. temps_preparation(),f.etapes(),).save()
   """
    recettes = Recette.objects.all()
    paginator = Paginator(recettes, 4)
    p = request.GET.get('p')
    try:
        recettePage = paginator.page(p)
    except PageNotAnInteger:
        recettePage = paginator.page(1)
    except EmptyPage:
        recettePage = paginator.page(paginator.num_pages)

    return render(request, 'recettes.html', {'recettes': recettePage})


def create_recette(request):
    if request.method == 'POST':
        form = RecetteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/recettes')

    else:
        form = RecetteForm()
    return render(request, 'create_recette.html', {'form': form})


def delete_recette(request, pk):
    recette = get_object_or_404(Recette, pk=pk)
    recette.delete()
    return redirect('/recettes')


def update_recette(request, pk):
    recette = get_object_or_404(Recette, pk=pk)
    if request.method == 'POST':
        form = RecetteForm(request.POST, instance=recette)
        if form.is_valid():
            form.save()
            return redirect('/recettes')

    else:
        form = RecetteForm()
    return render(request, 'update_recette.html', {'form': form, 'recette': recette})


def list_personne(request):
    """""
    for i in range(10):
        Recette(None,f.titre(),f. temps_preparation(),f.etapes(),).save()
   """
    # print("hellooooooooooooooooooooooo")
    personnes = Personne.objects.all()
    paginator = Paginator(personnes, 6)
    p = request.GET.get('p')
    try:
        personnePage = paginator.page(p)
    except PageNotAnInteger:
        personnePage = paginator.page(1)
    except EmptyPage:
        personnePage = paginator.page(paginator.num_pages)

    return render(request, 'personnes.html', {'personnes':personnePage})

def create_personne(request):
    if request.method == 'POST':
        form = PersonneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/personnes')
    else:
        form = PersonneForm()
    return render(request, 'create_personne.html', {'form': form})


def delete_personne(request, pk):
    personne = get_object_or_404(Personne, pk=pk)
    personne.delete()
    return redirect('/personnes')


def update_personne(request, pk):
    personne = get_object_or_404(Personne, pk=pk)
    if request.method == 'POST':
        form = PersonneForm(request.POST, instance=personne)
        if form.is_valid():
            form.save()
            return redirect('/personnes')
    else:
        form = PersonneForm()
    return render(request, 'update_personne.html', {'form': form, 'personne': personne})


def list_tag(request):
    """""
    for i in range(10):
        Recette(None,f.titre(),f. temps_preparation(),f.etapes(),).save()
   """
    tags = Tag.objects.all()
    paginator = Paginator(tags, 5)
    p = request.GET.get('p')
    try:
        tagPage = paginator.page(p)
    except PageNotAnInteger:
        tagPage = paginator.page(1)
    except EmptyPage:
        tagPage = paginator.page(paginator.num_pages)

    return render(request, 'tags.html', {'tags': tagPage})


def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tags')
    else:
        form = TagForm()
    return render(request, 'create_tag.html', {'form': form})


def delete_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    tag.delete()
    return redirect('/tags')


def update_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('/tags')
    else:
        form = TagForm()
    return render(request, 'update_tag.html', {'form': form, 'tag': tag})


def list_note(request):
    """""
    for i in range(10):
        Recette(None,f.titre(),f. temps_preparation(),f.etapes(),).save()
   """
    # print("hellooooooooooooooooooooooo")
    notes = Note.objects.all()
    paginator = Paginator(notes, 5)
    p = request.GET.get('p')
    try:
        notePage = paginator.page(p)
    except PageNotAnInteger:
        notePage = paginator.page(1)
    except EmptyPage:
        notePage = paginator.page(paginator.num_pages)

    return render(request, 'notes.html', {'notes': notePage})


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/notes')
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})


def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('/notes')


def update_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('/notes')
    else:
        form = NoteForm()
    return render(request, 'update_note.html', {'form': form, 'note': note})


def list_image(request):
    """""
    for i in range(10):
        Recette(None,f.titre(),f. temps_preparation(),f.etapes(),).save()
   """

    images = Image.objects.all()
    paginator = Paginator(images, 5)
    p = request.GET.get('p')
    try:
        imagePage = paginator.page(p)
    except PageNotAnInteger:
        imagePage = paginator.page(1)
    except EmptyPage:
        imagePage = paginator.page(paginator.num_pages)

    return render(request, 'images.html', {'images': imagePage})


def create_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/images')
    else:
        form = ImageForm()
    return render(request, 'create_image.html', {'form': form})


def delete_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    image.delete()
    return redirect('/images')


def update_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, instance=image)
        if form.is_valid():
            form.save()
            return redirect('/images')
    else:
        form = ImageForm()
    return render(request, 'update_image.html', {'form': form, 'image': image})


def list_commentaire(request):
    """""
    for i in range(10):
        Recette(None,f.titre(),f. temps_preparation(),f.etapes(),).save()
   """
    # print("hellooooooooooooooooooooooo")

    commentaires = Commentaire.objects.all()
    paginator = Paginator(commentaires, 5)
    p = request.GET.get('p')
    try:
        commentairePage = paginator.page(p)
    except PageNotAnInteger:
        commentairePage = paginator.page(1)
    except EmptyPage:
        commentairePage = paginator.page(paginator.num_pages)

    return render(request, 'commentaires.html', {'commentaires': commentairePage})


def create_commentaire(request):
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/commentaires')
    else:
        form = CommentaireForm()
    return render(request, 'create_commentaire.html', {'form': form})


def delete_commentaire(request, pk):
    commentaire = get_object_or_404(Commentaire, pk=pk)
    commentaire.delete()
    return redirect('/commentaires')


def update_commentaire(request, pk):
    commentaire = get_object_or_404(Commentaire, pk=pk)
    if request.method == 'POST':
        form = CommentaireForm(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
            return redirect('/commentaires')
    else:
        form = CommentaireForm()
    return render(request, 'update_commentaire.html', {'form': form, 'commentaire': commentaire})

def list_personne(request):
    """""
    for i in range(10):
        Recette(None,f.titre(),f. temps_preparation(),f.etapes(),).save()
   """
    # print("hellooooooooooooooooooooooo")
    personnes = Personne.objects.all()
    paginator = Paginator(personnes, 6)
    p = request.GET.get('p')
    try:
        personnePage = paginator.page(p)
    except PageNotAnInteger:
        personnePage = paginator.page(1)
    except EmptyPage:
        personnePage = paginator.page(paginator.num_pages)

    return render(request, 'personnes.html', {'personnes':personnePage})

def create_personne(request):
    if request.method == 'POST':
        form = PersonneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/personnes')
    else:
        form = PersonneForm()
    return render(request, 'create_personne.html', {'form': form})


def delete_personne(request, pk):
    personne = get_object_or_404(Personne, pk=pk)
    personne.delete()
    return redirect('/personnes')


def update_personne(request, pk):
    personne = get_object_or_404(Personne, pk=pk)
    if request.method == 'POST':
        form = PersonneForm(request.POST, instance=personne)
        if form.is_valid():
            form.save()
            return redirect('/personnes')
    else:
        form = PersonneForm()
    return render(request, 'update_personne.html', {'form': form, 'personne': personne})

def list_ingredient(request):
    """""
    for i in range(10):
        Recette(None,f.titre(),f. temps_preparation(),f.etapes(),).save()
   """
    ingredients = Ingredient.objects.all()
    paginator = Paginator(ingredients, 4)
    p = request.GET.get('p')
    try:
        ingredientPage = paginator.page(p)
    except PageNotAnInteger:
        ingredientPage = paginator.page(1)
    except EmptyPage:
        ingredientPage = paginator.page(paginator.num_pages)

    return render(request, 'ingredients.html', {'ingredients':ingredientPage})


def create_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ingredients')

    else:
        form = IngredientForm()
    return render(request, 'create_ingredient.html', {'form': form})


def delete_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    ingredient.delete()
    return redirect('/ingredients')


def update_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('/ingredients')

    else:
        form = IngredientForm()
    return render(request, 'update_ingredient.html', {'form': form, 'ingredient': ingredient})



def scrap_page(request):
    """recipes_list = scrape('recipe/26670/taylors-piroshki/', 2)"""
    """with open('myapp/scrapper/recipes.json', 'r') as f:
        data = json.load(f)"""
    if request.method == 'POST':
        try:
            num_to_scrape = int(request.POST.get('num_of_recipes', ''))
            print(num_to_scrape)
        except Exception as e:
            return render(request, 'scrape_data.html', {'error' : e, 'success' : None})
        try :
            starting_points = ['recipe/26670/taylors-piroshki/', 'recipe/257538/authentic-tacos-al-pastor/', 'recipe/25805/churros-ii/', 'recipe/262717/indian-chole-aloo-tikki/', 'recipe/263690/easy-chicken-yakitori/', 'recipe/141370/mexican-strawberry-water-agua-de-fresa/', 'recipe/254743/taameya-egyptian-falafel/']
            
            data = scrape(starting_points[random.randint(0, 6)], num_to_scrape)
            with open('myapp/scrapper/recipes.json', 'w') as f:
                json.dump(data, f)
            """with open('myapp/scrapper/recipes.json', 'r') as f:
                data = json.load(f)"""
            importData(data)
            return render(request, 'scrape_data.html', {'success' : 'Data scrapped successfully!', 'error' : None})
        except Exception as e:
            print(e)
        
    else :
        return render(request, 'scrape_data.html', {'error' : None, 'success' : None})
    