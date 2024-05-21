# Generated by Django 3.0.7 on 2024-05-21 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20240520_2339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conta',
            old_name='saldo',
            new_name='saldo_real',
        ),
        migrations.AddField(
            model_name='conta',
            name='saldo_bitcoin',
            field=models.DecimalField(decimal_places=8, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]