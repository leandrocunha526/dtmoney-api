from django.urls import path
from .views import TransactionView, RegisterTransactionView, DeleteTransactionView, UpdateTransactionView, GetByIdTransactionView

urlpatterns = [
    path('list/', TransactionView.as_view({'get': 'list'}), name='List transaction'),
    path('register/', RegisterTransactionView.as_view(), name="Register transaction"),
    path('delete/<pk>/', DeleteTransactionView, name="Delete transaction"),
    path('update/<pk>/', UpdateTransactionView, name="Update transaction"),
    path('details/<pk>/', GetByIdTransactionView, name="Get by id transaction"),
]
