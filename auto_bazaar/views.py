from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView,DetailView, UpdateView
from .models import Car, Brand

# Create your views from here
class CarListView(CreateView):
    def get(self, request):
        cars = Car.objects.all()
        brands = Brand.objects.all()
        return render(request, 'car_list.html', {'cars': cars, 'brands': brands})

class CarDetailView(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

class PurchaseCarView(UpdateView):
    def post(self, request, id):
        car = get_object_or_404(Car, pk=id)

        # Check if the car is in stock
        if car.quantity > 0:
            # Reduce the quantity by one and save the changes
            car.quantity -= 1
            car.save()

            return redirect('car_detail', pk=car.id)
        else:
            # If the car is out of stock, you might want to handle this case appropriately
            return render(request, 'out_of_stock.html')  # Create this template