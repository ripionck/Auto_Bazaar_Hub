from django.urls import path
from .views import CarListView,FilteredCarsListView, CarDetailView, PurchaseCarView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('filtered_cars/', FilteredCarsListView.as_view(), name='filtered_cars_all'),
    path('filtered_cars/<int:brand_id>/', FilteredCarsListView.as_view(), name='filtered_cars'),
    path('details/<int:id>/', CarDetailView.as_view(), name='car_detail'),
    path('purchase/<int:id>/', PurchaseCarView.as_view(), name='purchase_car'),
]
