# Generated by Django 4.1.1 on 2022-09-09 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transaction", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="amount",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
