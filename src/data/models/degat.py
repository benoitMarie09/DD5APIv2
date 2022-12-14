from django.db import models
from .base import BaseModel


class Degat(models.Model):
    bonus = models.IntegerField(default=0)
    de = models.CharField('dé de dégat', default='1d6', max_length=50)
    type = models.ForeignKey("TypeDegat", blank=True,
                             null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['type']

    def __str__(self):
        if self.bonus == 0:
            return f'{self.de}({self.type.index})'
        return f'{self.de}+{self.bonus}({self.type.index})'


class TypeDegat(BaseModel):
    pass


class Soin(models.Model):
    bonus = models.IntegerField(default=0)
    bonus_mod = models.BooleanField(default=False)
    de = models.CharField('dé de dégat', default='1d6', max_length=50)
    type = models.ForeignKey("TypeDegat", blank=True,
                             null=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.bonus == 0:
            if self.bonus_mod:
                return f'{self.de}({self.type.index}) + MOD'
        if self.bonus_mod:
            return f'{self.de}+{self.bonus}({self.type.index}) + MOD'
        return f'{self.de}+{self.bonus}({self.type.index})'


class DegatSortEmplacements(models.Model):
    desc = models.TextField(null=True, blank=True)
    emplacement_nv0 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv0')
    emplacement_nv1 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv1')
    emplacement_nv2 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv2')
    emplacement_nv3 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv3')
    emplacement_nv4 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv4')
    emplacement_nv5 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv5')
    emplacement_nv6 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv6')
    emplacement_nv7 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv7')
    emplacement_nv8 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv8')
    emplacement_nv9 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv9')

class DegatSortNiveaux(models.Model):
    desc = models.TextField(null=True, blank=True)
    niveau_0 = models.ManyToManyField('Degat',blank=True,related_name='niveau_0')
    niveau_5 = models.ManyToManyField('Degat',blank=True,related_name='niveau_1')
    niveau_11 = models.ManyToManyField('Degat',blank=True,related_name='niveau_2')
    niveau_17 = models.ManyToManyField('Degat',blank=True,related_name='niveau_3')



    
class SoinSortEmplacements(models.Model):
    desc = models.TextField(null=True, blank=True)
    emplacement_nv0 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv0')
    emplacement_nv1 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv1')
    emplacement_nv2 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv2')
    emplacement_nv3 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv3')
    emplacement_nv4 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv4')
    emplacement_nv5 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv5')
    emplacement_nv6 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv6')
    emplacement_nv7 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv7')
    emplacement_nv8 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv8')
    emplacement_nv9 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv9')
