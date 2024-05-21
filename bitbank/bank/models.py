from django.db import models

class Conta(models.Model):
    nome = models.CharField(max_length=30, verbose_name="Nome da Conta")
    saldo_real = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Saldo em Reais")
    saldo_bitcoin = models.DecimalField(max_digits=10, decimal_places=8, verbose_name="Saldo em Bitcoin")
    saldo_ethereum = models.DecimalField(max_digits=28, decimal_places=18, verbose_name="Saldo em Ethereum")

    def __str__(self):
        return self.nome


    



