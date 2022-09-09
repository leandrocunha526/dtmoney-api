from rest_flex_fields import FlexFieldsModelSerializer

from transaction.models import Transaction


class TransactionSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
