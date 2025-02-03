from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm

 # print(request)
    # print(request.GET)
    # filtros
    # cars = Car.objects.filter(brand=2) # filtrando por id da brand (marcas)
    # cars = Car.objects.filter(brand__name='Fiat') # filtrando pelo nome da brand
    # cars = Car.objects.filter(model__contains='Chevette') # filtrando pelo modelo se contiver Chevette
    # cars = Car.objects.filter(model__icontains='Chevette') # filtrando ignorando o CamelCase
    # cars = Car.objects.all().order_by('-model') # ordenação invertidada

    # http://127.0.0.1:8000/cars/?search=marea # busca pelo modelo do carro

# Create your views here.
def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        cars = cars.filter(model__icontains=search)

    return render(
        request, 
        'cars.html',
        {'cars': cars }
    )

def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarForm(request.POST, request.FILES)
        # print(new_car_form.data)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list') 
    else:
        new_car_form = CarForm()
    
    return render(request, 'new_car.html', {'new_car_form': new_car_form})