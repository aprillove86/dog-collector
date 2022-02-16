from django.shortcuts import render

# Create your views here.
class Dog:
    def __init__(self, name, breed, temperment):
        self.name = name
        self.breed = breed
        self.temperment = temperment

dogs = [
    Dog('Violet', 'Frenchie', 'super chill'),
    Dog('Guapo', 'Husky', 'goofy'),
    Dog('Pac', 'Staffordshire', 'protective'),
]
## create views

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})