from django.shortcuts import render
from django.http import HttpResponse

class Pet:
    def __init__(self, name, kingdom, species, common_name, age, height, weight)
        self.name = name
        self.kingdom = kingdom
        self.species = species
        self.common_name = common_name
        self.age = age
        self.height = height
        self.weight = weight

pets = [
    Pet('Johnny', 'Animalia', 'Bradypus tridactylus', '5 Toed Sloth', 42, 71, 185),
    Pet('Weronica', 'Animalia', 'C. corax', 'Raven', 7, 12, 1),
    Pet('Huisoo', 'Plantae', 'S. japonica', 'Serissa', 8, 20, 10),
    Pet('')
]


# Create your views here.
def home(request):
    return HttpResponse('Hello! Welcome to Human Pet Collector. This is a safe space for anyone who feels like human interactions fall short of relationships with pets to meet friends hopefully as loving and loyal as your pet.')

def about(request):
    return render(request, 'about.html')

def pets(request):
    return HttpResponse('This is a page for all Human Pets registered on site')

def mypets(request):
    return HttpResponse('This is a page for all Human Pets belonging to user')

