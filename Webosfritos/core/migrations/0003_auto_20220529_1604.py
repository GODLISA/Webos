# Generated by Django 2.1.2 on 2022-05-29 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220529_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Usuario'),
        ),
    ]
