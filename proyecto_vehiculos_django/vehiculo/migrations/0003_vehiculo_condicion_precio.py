# Generated by Django 4.0.5 on 2023-08-06 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_alter_vehiculo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='condicion_precio',
            field=models.CharField(choices=[('bajo', 'Bajo'), ('medio', 'Medio'), ('alto', 'Alto')], default='bajo', max_length=10),
        ),
    ]
