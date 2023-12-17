from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView,DetailView, UpdateView, ListView
from .models import Car, Brand
from .forms import CommentForm
from django.urls import reverse_lazy

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
    
class CarDetailView(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=request.POST)
        car = self.get_object()

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user  # Assuming you have a user associated with the request
            new_comment.car = car
            new_comment.save()

            # Redirect to the same page to avoid form resubmission
            return redirect('car_detail', id=car.id)

        return self.get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()  # Assuming you have a related_name='comments' in your Comment model
        comment_form = CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

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
        
