from django.db import models

# Create your models here.

class Personne(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def check_password(self, password):
        return self.password == password

class ProfileUtilisateur(Personne):
    adresse = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)


class Tag(models.Model):
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle


class Recette(models.Model):
    titre = models.CharField(max_length=50)
    description = models.CharField(max_length=800)
    tag = models.ForeignKey( Tag ,on_delete=models.CASCADE )
    personnes = models.ManyToManyField(Personne, through='AssociationCommentaire')

    def __str__(self):
        return self.titre

class Image(models.Model):
    url = models.CharField(max_length=300)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)

class Ingredient(models.Model):
    text = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Information(models.Model):
    key = models.CharField(max_length=30)
    value = models.CharField(max_length=50)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)


class Etape(models.Model):
    text = models.CharField(max_length=800)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)

"""class Commentaire(models.Model):
    contenu = models.TextField()"""

class AssociationCommentaire(models.Model):
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    commentaire = models.TextField()
    note = models.IntegerField()

    def __str__(self):
        return f"Le commentaire de {self.personne.nom} sur la recette :{self.recette.titre}"
