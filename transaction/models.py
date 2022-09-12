from django.db import models


class Transaction(models.Model):
    class Meta:
        verbose_name_plural = "Transactions"
    title = models.CharField(max_length=300)
    type = models.CharField(max_length=300)
    category = models.CharField(max_length=300)
    amount = models.IntegerField()
    date = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-createdAt']

    # The __str__ method in Python represents the class objects as a string it can be used for classes.
    def __str__(self):
        return self.title
