# Generated by Django 5.0.6 on 2024-11-10 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoValidador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estado', models.CharField(max_length=100)),
                ('descripcion_estado', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ubicacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Validador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie_val', models.IntegerField(unique=True)),
                ('amid_val', models.IntegerField(unique=True)),
                ('modelo', models.CharField(blank=True, max_length=5, null=True)),
                ('id_usuario', models.IntegerField()),
                ('fecha_creacion', models.DateField()),
                ('id_estado_validador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='validadores.estadovalidador')),
                ('id_ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='validadores.ubicacion')),
            ],
        ),
    ]
