# Generated by Django 4.0.2 on 2022-05-31 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_usuario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='idreceta',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='receta',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
