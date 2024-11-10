# Generated by Django 5.0.6 on 2024-11-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim_msisdn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simmsisdn',
            name='usuario_apellido',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='simmsisdn',
            name='usuario_correo',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='simmsisdn',
            name='usuario_nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
