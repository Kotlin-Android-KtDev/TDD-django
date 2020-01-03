from django.db import models

class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None ,on_delete=models.CASCADE)
    #when used ForiegnKey there have some error but can fig by "on_delete=models.CASCADE"