from django.db import models


class QuantiteMonaie(models.Model):
    quantite = models.IntegerField()
    monaie = models.ForeignKey(
        'Monaie', default='Po', null=True, on_delete=models.CASCADE)
    equipement = models.ForeignKey(
        'Equipement', blank=True, null=True, related_name='prix', on_delete=models.CASCADE)
    historique = models.ForeignKey(
        'Historique', blank=True, null=True, related_name='monaie_de_depart', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantite} {self.monaie}"



class QuantiteEquipement(models.Model):
    quantite = models.IntegerField(default=1)
    equipement = models.ForeignKey(
        'Equipement', related_name='quantite', blank=True, null=True, on_delete=models.CASCADE)
    historique = models.ForeignKey(
        'Historique', related_name='quantite_equipement', blank=True, null=True, on_delete=models.CASCADE)
    classe = models.ForeignKey(
        'Classe', related_name='quantite_equipement', blank=True, null=True, on_delete=models.CASCADE)
    pack_equipement = models.ForeignKey(
        'PackEquipementClasse', related_name='contenu_pack', blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.quantite}"


class QuantiteEquipementAventurier(models.Model):
    quantite = models.IntegerField(default=1)
    equipement = models.ForeignKey(
        'EquipementAventurier', related_name='quantite_equipement_aventurier', blank=True, null=True, on_delete=models.CASCADE)
    sac = models.ForeignKey(
        'Sac', related_name='quantite_equipement_aventurier', blank=True, null=True, on_delete=models.CASCADE)


class QuantiteSpecifique(models.Model):
    valeur = models.DecimalField(
        decimal_places=2, max_digits=4, null=True, blank=True)
    quantite = models.IntegerField(default=1,blank=True, null=True)
    specifique = models.ForeignKey(
        'Specifique', null=True, blank=True, on_delete=models.CASCADE)
    niveau = models.ForeignKey(
        'Niveau', null=True, blank=True,related_name='specifique', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.quantite}"


class ValeurCaracteristique(models.Model):
    valeur = models.IntegerField(default=1)
    caracteristique = models.ForeignKey(
        'Caracteristique', related_name='valeur_caract', blank=True, null=True, on_delete=models.CASCADE)
    race = models.ForeignKey(
        'Race', related_name='caracteristique', blank=True, null=True, on_delete=models.CASCADE)
    prerequis = models.ForeignKey(
        'PrerequisCaracteristique', related_name='valeur_caract', blank=True, null=True, on_delete=models.CASCADE)
    monstre = models.ForeignKey(
        'Monstre', related_name='valeur_caract1', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: +{}'.format(self.caracteristique, self.valeur)

