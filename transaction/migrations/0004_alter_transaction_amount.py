# Generated by Django 4.1.1 on 2022-09-11 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transaction", "0003_alter_transaction_createdat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="amount",
            field=models.IntegerField(),
        ),
    ]
