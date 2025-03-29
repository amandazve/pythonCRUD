from django.shortcuts import render, redirect
from app.forms import PersonForm
from app.models import Person
from django.core.paginator import Paginator 

# Create your views here.
def home(request):
    data = {}
    all = Person.objects.all()
    paginator = Paginator(all, 5) #Paginação com a quantidade de itens informados
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)

    search = request.GET.get('search')
    if search:
        data['db'] = Person.objects.filter(FirstName__icontains=search)
    else:
        data['db'] = Person.objects.all()
    return render(request, 'index.html', data)
    ## data['db'] = Person.objects.all()

def form(request):
    data = {}
    data['form'] = PersonForm()
    return render(request, 'form.html', data)

from django.shortcuts import render, redirect
from .forms import PersonForm

def create(request):
    form = PersonForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'create.html', {'form': form})  # Renderiza o template

def view(request, pk):
    data = {}
    data['db'] = Person.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Person.objects.get(pk=pk)
    data['form'] = PersonForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Person.objects.get(pk=pk)
    form = PersonForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')

def delete(request, pk):
    db = Person.objects.get(pk=pk)
    db.delete()
    return redirect('home')
