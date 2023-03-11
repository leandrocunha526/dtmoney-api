from rest_flex_fields.views import FlexFieldsMixin
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from rest_framework import generics


class TransactionView(FlexFieldsMixin, ReadOnlyModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class RegisterTransactionView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


@api_view(['DELETE'])
def DeleteTransactionView(request, pk):
    transaction = Transaction.objects.get(id=pk)
    transaction.delete()
    return Response("The " + pk + " was successfully deleted", status=status.HTTP_200_OK)


@api_view(['PUT'])
def UpdateTransactionView(request, pk):
    transaction = Transaction.objects.get(id=pk)
    serializer = TransactionSerializer(transaction, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetByIdTransactionView(request, pk):
    transaction = Transaction.objects.get(id=pk)
    serializer = TransactionSerializer(transaction, many=False)
    return Response(serializer.data)
