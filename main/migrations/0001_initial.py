# Generated by Django 4.1.5 on 2023-01-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomecomp', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PessoaJ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.IntegerField()),
            ],
        ),
    ]
