# Generated by Django 3.1.3 on 2020-11-28 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.PositiveIntegerField()),
                ('detpo', models.CharField(default=True, max_length=100)),
                ('detalle', models.CharField(default=True, max_length=300)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=150)),
                ('dni', models.CharField(max_length=20)),
                ('mail', models.EmailField(default=True, max_length=254)),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.direccion')),
            ],
        ),
    ]
