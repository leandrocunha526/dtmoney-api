# Generated by Django 4.1.1 on 2022-09-09 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=300)),
                ("type", models.CharField(max_length=300)),
                ("category", models.CharField(max_length=300)),
                ("amount", models.PositiveIntegerField()),
                ("date", models.DateTimeField()),
                ("createdAt", models.DateField(auto_now=True)),
            ],
            options={
                "ordering": ["-createdAt"],
            },
        ),
    ]
