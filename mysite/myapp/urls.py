from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('recettes/', list_recette , name='recette'),
    path('recettes/create/', create_recette , name='create_recette'),
    path('recettes/delete/<int:pk>', delete_recette, name='delete_recette'),
    path('recettes/update/<int:pk>', update_recette, name='update_recette'),
    path('personnes/', list_personne, name='personne'),
    path('personnes/create/', create_personne, name='create_personne'),
    path('personnes/delete/<int:pk>', delete_personne, name='delete_personne'),
    path('personnes/update/<int:pk>', update_personne, name='update_personne'),
    path('tags/', list_tag, name='tag'),
    path('tags/create/', create_tag, name='create_tag'),
    path('tags/delete/<int:pk>', delete_tag, name='delete_tag'),
    path('tags/update/<int:pk>', update_tag, name='update_tag'),
    path('images/', list_image, name='image'),
    path('images/create/', create_image, name='create_image'),
    path('images/delete/<int:pk>', delete_image, name='delete_image'),
    path('images/update/<int:pk>', update_image, name='update_image'),
    path('commentaires/', list_commentaire, name='commentaire'),
    path('commentaires/create/', create_commentaire, name='create_commentaire'),
    path('commentaires/delete/<int:pk>', delete_commentaire, name='delete_commentaire'),
    path('commentaires/update/<int:pk>', update_commentaire, name='update_commentaire'),
    path('ingredients/', list_ingredient , name='ingredient'),
    path('ingredients/create/', create_ingredient , name='create_ingredient'),
    path('ingredients/delete/<int:pk>', delete_ingredient, name='delete_ingredient'),
    path('ingredients/update/<int:pk>', update_ingredient, name='update_ingredient'),
    path('scrape/', scrap_page, name='scrap_page')
]
