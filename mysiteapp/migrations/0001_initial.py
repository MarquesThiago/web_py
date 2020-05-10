# Generated by Django 3.0.6 on 2020-05-10 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Habilidade',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('nascimento', models.DateField()),
                ('antiguidade', models.IntegerField(default=0)),
                ('id_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysiteapp.Departamento')),
                ('id_habilidades', models.ManyToManyField(to='mysiteapp.Habilidade')),
            ],
        ),
    ]