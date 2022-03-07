from django.urls import path

from baskets.views import basket_add, basket_remove, basket_clean, basket_edit

app_name = 'baskets'

urlpatterns = [
    path('basket-add/<int:id>/', basket_add, name='basket_add'),
    path('basket-remove/<int:id>/', basket_remove, name='basket_remove'),
    path('basket-clean/', basket_clean, name='basket_clean'),
    path('basket-edit/<int:id>/<int:quantity>/', basket_edit, name='basket_edit')
]