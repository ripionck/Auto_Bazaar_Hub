from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView,DetailView, UpdateView, ListView
from .models import Car, Brand, Order
from .forms import CommentForm


# Create your views from here
class CarListView(CreateView):
    def get(self, request):
        cars = Car.objects.all()
        brands = Brand.objects.all()
        return render(request, 'car_list.html', {'cars': cars, 'brands': brands})

class FilteredCarsListView(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'cars'

    def get_queryset(self):
        brand_id = self.kwargs.get('brand_id')
        if brand_id:
            queryset = Car.objects.filter(brand__id=brand_id)
        else:
            queryset = Car.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context
    
class CarDetailView(DetailView, CreateView):
    model = Car
    template_name = 'car_details.html'
    context_object_name = 'car'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()

        if car:
            context['car'] = car
            comments = car.comments.all() if hasattr(car, 'comments') else []
            comment_form = CommentForm()

            context['comments'] = comments
            context['comment_form'] = comment_form

        return context

    def form_valid(self, form):
        car = self.get_object()
        
        if car:
            form.instance.user = self.request.user
            form.instance.car = car
            form.save()
            return redirect('car_detail', pk=car.pk)
        else:
            # Handle the case when the car does not exist
            return redirect('homepage')  

class PurchaseCarView(UpdateView):
    def post(self, request, *args, **kwargs):
        car_id = kwargs.get('id')
        
        # Use get_object_or_404 to retrieve the Car object or return a 404 response
        car = get_object_or_404(Car, id=car_id)

        # Check if the car is in stock
        if car.quantity > 0:
            # Create an order record for the user
            order = Order(user=request.user, car=car)
            order.save()

            # Reduce the quantity by one and save the changes
            car.quantity -= 1
            car.save()

            return redirect('car_detail', pk=car.id)
        else:
            # If the car is out of stock, you might want to handle this case appropriately
            return render(request, 'out_of_stock.html')
