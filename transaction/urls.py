from django.urls import path
from .views import TransactionView, RegisterTransactionView, DeleteTransactionView, UpdateTransactionView

urlpatterns = [
    path('list/', TransactionView.as_view({'get': 'list'}), name='List transaction'),
    path('register/', RegisterTransactionView.as_view(), name="Register transaction"),
    path('delete/<str:pk>/', DeleteTransactionView, name="Delete transaction"),
    path('update/<str:pk>/', UpdateTransactionView, name="Update transaction"),
]
