from django.shortcuts import render, redirect
from .models import Dog
from .models import Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm

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
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})
   
def toys_index(request):
    toys = Toy.objects.all()
    return render(request, 'toys/index.html', {'toys': toys})

def dogs_detail(request, dog_id):
   dog = Dog.objects.get(id=dog_id)
   feeding_form = FeedingForm()
   
   toys_dog_doesnt_have = Toy.objects.exclude(id__in = dog.toys.all().values_list('id'))

   return render(request, 'dogs/detail.html',
   {'dog': dog, 
   'feeding_form': feeding_form,
   'toys': toys_dog_doesnt_have
    })

def add_feeding(request, dog_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False) 
        new_feeding.dog_id = dog_id
        new_feeding.save()
    return redirect('detail', dog_id=dog_id)

def toys_detail(request, toy_id):
   toy = Toy.objects.get(id=toy_id)
   return render(request, 'toys/detail.html', {'toy': toy })

def assoc_toy(request, dog_id, toy_id):
   Dog.objects.get(id=dog_id).toys.add(toy_id)
   return redirect('detail', dog_id=dog_id)



class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

    # fat models, skinny controllers

class DogUpdate(UpdateView):
    model = Dog
    fields = ('name', 'breed', 'temperment')
class ToyUpdate(UpdateView):
    model = Toy
    fields = ('name', 'color')


class DogDelete(DeleteView):
    model = Dog
    success_url ='/dogs/'
class ToyDelete(DeleteView):
    model = Toy
    success_url ='/toys/'

