# Generated by Django 4.2 on 2023-06-03 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0009_alter_clientes_fecha_de_realizacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='fecha_de_realizacion',
            field=models.DateField(default=datetime.date(2023, 6, 3)),
        ),
    ]