from django.db import models

from django.contrib.auth.models import User

class List(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    list_name = models.CharField(max_length=100)
    list_description = models.TextField(blank=True)
    

    class Meta:
        verbose_name = ("List")
        verbose_name_plural = ("Lists")

    def __str__(self):
        return self.list_name

    def get_absolute_url(self):
        return reverse("List_detail", kwargs={"pk": self.pk})


class Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_description = models.TextField(blank=True)

    class Meta:
        verbose_name = ("Item")
        verbose_name_plural = ("Items")

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("Item_detail", kwargs={"pk": self.pk})
