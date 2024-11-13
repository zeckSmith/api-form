from django.db import models

# Create your models here.
from django.db import models

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    code_client = models.CharField(max_length=10, unique=True, verbose_name="Code client unique")
    statut = models.BooleanField(default=False, verbose_name="Statut de soumission du formulaire")

    #la  methode qui verifie la soumission d'un formulaire
    class Meta:
        db_table = 'client'
    def __str__(self):
        return f"Client {self.code_client} - Statut: {'Soumis' if self.statut else 'Non soumis'}"


class FormulaireClient(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, db_column="client_id", verbose_name="Client associé")
    q1 = models.IntegerField(verbose_name="Question 1")
    q2 = models.IntegerField(verbose_name="Question 2")
    q3 = models.IntegerField(verbose_name="Question 3")
    q4 = models.IntegerField(verbose_name="Question 4")
    q5 = models.IntegerField(verbose_name="Question 5")
    q6 = models.CharField(max_length=150)
    q7 = models.IntegerField(verbose_name="Question 6")
    q8 = models.IntegerField(verbose_name="Question 7")
    q9 = models.IntegerField(verbose_name="Question 8")
    q10 = models.IntegerField(verbose_name="Question 9")
    q11 = models.IntegerField(verbose_name="Question 10")
    q12 = models.CharField(max_length=255)
    q13 = models.IntegerField(verbose_name="Question 11")
    q14 = models.IntegerField(verbose_name="Question 12")
    q15 = models.CharField(max_length=10)
    q16 = models.CharField(max_length=255)
    q17 = models.CharField(max_length=10)
    q18 = models.CharField(max_length=10)
    q19 = models.CharField(max_length=255, null=True, blank=True)
    date_soumission = models.DateTimeField(auto_now_add=True, verbose_name="Date de soumission")
    # date_cr = models.CharField(max_length=10)
    # q3 = models.TextField(max_length=255, verbose_name="Commentaire")

    class Meta:
        db_table = 'formulaire_client'
    
    def __str__(self):
        return f"Formulaire pour {self.client.code_client} - Date : {self.date_soumission}"




