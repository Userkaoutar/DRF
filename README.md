Django REST Framework

Ce guide détaille les étapes que j'ai suivi pour créer une API RESTful simple à l'aide de Django REST Framework dans mon projet django_rest_beginners.


##Étapes de configuration

##1. Installation de Django et Django REST Framework

```bash
pip install django
pip install djangorestframework

```
##2. Création du projet Django


```bash
django-admin startproject django_rest_beginners
```

##3. Création de l'application Django

```bash
python manage.py startapp api
```

Dans settings.py, j'ai ajouté 'rest_framework' pour intégrer le framework Django REST, et 'api.apps.ApiConfig' pour configurer mon application api.


```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'rest_framework',
]
```

##4. Configuration des modèles de données

Les modèles dans Django REST Framework sont essentiellement des classes Python qui définissent la structure des données de notre application

Pour les modèles, j'ai créé deux classes : Location et Item. Location comporte un champ name, tandis que Item comprend des champs name, date_added, et une clé étrangère location pointant vers Location.

```bash
class Location(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=150)
    date_added = models.DateField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
```

Dans le fichier admin.py, j'ai importé les modèles Item et Location de mon application Django et les ai enregistrés dans l'interface d'administration à l'aide de la méthode register(). 
Cela permet à l'administrateur d'accéder et de gérer ces modèles via l'interface d'administration de manière pratique.

```bash
admin.site.register(Item)
admin.site.register(Location)
```

<img width="905" alt="image" src="https://github.com/Userkaoutar/DRF/assets/101696114/9718d46f-b70e-4cb7-a141-59bb7267aeb6">


##5. Sérialisation des données

J'ai créé des sérialiseurs dans le fichier serializers.py de mon application pour transformer les modèles Django en JSON et vice versa.

```bash
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')

```
##6. Définition des vues


Ce fichier contient des vues génériques de Django REST Framework pour interagir avec les modèles Location et Item. Les vues ItemList et ItemDetail
sont utilisées pour lister, créer, récupérer, mettre à jour et supprimer des éléments,
tandis que les vues LocationList et LocationDetail font de même pour les emplacements. 
Elles simplifient le processus de création d'une API RESTful en utilisant les fonctionnalités fournies par DRF.

```bash
class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

```
##7. Configuration des URLs

J'ai configuré les URL dans le fichier urls.py de mon application pour mapper les vues aux endpoints de mon API.

```bash
urlpatterns = [
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
]
```
##8. Test de l'API

J'ai exécuté mon serveur de développement Django et j'ai testé mon API en accédant aux endpoints définis dans mes URLs.

```bash
python manage.py runserver

```

<img width="920" alt="image" src="https://github.com/Userkaoutar/DRF/assets/101696114/2cc48000-d8de-4ad1-a3b7-226f2c8f3793">

.

<img width="875" alt="image" src="https://github.com/Userkaoutar/DRF/assets/101696114/960bd346-4f6f-4bb2-8087-ef2eba13f9d0">

.


<img width="878" alt="image" src="https://github.com/Userkaoutar/DRF/assets/101696114/2e33bc5b-b5af-46f1-bb74-23235505e1a6">

.


<img width="901" alt="image" src="https://github.com/Userkaoutar/DRF/assets/101696114/ed6ba16d-5bac-4f31-b89d-7e6ea84d5510">

 .



Conclusion

En résumé, ce guide explique comment j'ai utilisé Django REST Framework pour créer une API RESTful dans mon projet. 
J'ai installé les packages nécessaires, configuré les modèles de données, les sérialiseurs, les vues, et les URL, puis j'ai testé mon API.

