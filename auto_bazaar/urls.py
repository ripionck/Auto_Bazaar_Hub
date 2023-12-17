from django.urls import path
from .views import CarListView, CarDetailView, PurchaseCarView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('details/<int:id>/', CarDetailView.as_view(), name='car_detail'),
    path('purchase/<int:id>/', PurchaseCarView.as_view(), name='purchase_car'),
]
