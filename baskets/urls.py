from django.urls import path

from baskets.views import basket_add, basket_remove, basket_clean

app_name = 'baskets'

urlpatterns = [
    path('basket-add/<int:product_id>', basket_add, name='basket_add'),
    path('basket-remove/<int:id>', basket_remove, name='basket_remove'),
    path('basket-clean/', basket_clean, name='basket_clean')
]