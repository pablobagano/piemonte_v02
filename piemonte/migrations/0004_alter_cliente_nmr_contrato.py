# Generated by Django 4.2.3 on 2023-09-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("piemonte", "0003_cliente_data_contrato_cliente_duracao_contrato_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="nmr_contrato",
            field=models.CharField(max_length=20),
        ),
    ]
