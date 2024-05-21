# Generated by Django 3.0.7 on 2024-05-21 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20240520_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='conta',
            name='saldo_ethereum',
            field=models.DecimalField(decimal_places=18, default=1, max_digits=28, verbose_name='Saldo em Ethereum'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conta',
            name='nome',
            field=models.CharField(max_length=30, verbose_name='Nome da Conta'),
        ),
        migrations.AlterField(
            model_name='conta',
            name='saldo_bitcoin',
            field=models.DecimalField(decimal_places=8, max_digits=10, verbose_name='Saldo em Bitcoin'),
        ),
        migrations.AlterField(
            model_name='conta',
            name='saldo_real',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Saldo em Reais'),
        ),
    ]