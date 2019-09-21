from django.db import models


class Editor(models.Model):
    text = models.TextField(default='')
    dat = models.DateTimeField(auto_now=True)
