from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import re


def camel_to_snake(camel):
    camel = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', camel).lower()

def endpoint_case(snake):
    list = []
    for word in snake.split('_'): 
        if word == 'niveau':
            list.append('niveaux')
        elif word[-1] not in ('s','x'):
            list.append(word+'s')
        else:
            list.append(word)
    return '-'.join(list)+'-detail'


# Model de reference
class BaseModel(models.Model):
    nom = models.CharField(max_length=50)
    index = models.CharField(
        primary_key=True, max_length=50, default='default')
    desc = models.TextField('description', null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['index']

    def save(self, *args, **kwargs):
        self.index = slugify(self.nom)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.index

    def get_absolute_url(self):
        return reverse(endpoint_case(camel_to_snake(str(self.__class__.__name__))), kwargs={'pk': self.pk})
