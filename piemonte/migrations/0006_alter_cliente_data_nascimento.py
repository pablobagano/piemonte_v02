# Generated by Django 4.2.3 on 2023-09-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("piemonte", "0005_cliente_data_nascimento_cliente_sexo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="data_nascimento",
            field=models.DateField(default=None),
        ),
    ]
