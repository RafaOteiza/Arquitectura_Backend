# Generated by Django 5.0.6 on 2024-11-16 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validadores', '0003_historialubicacionesvalidador_usuario_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialubicacionesvalidador',
            name='id_movimiento',
            field=models.CharField(choices=[('Entrada', 'Entrada'), ('Salida', 'Salida')], max_length=10),
        ),
    ]
