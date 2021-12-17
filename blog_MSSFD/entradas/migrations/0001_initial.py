# Generated by Django 4.0 on 2021-12-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entradas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='DEFAULT_VALUE', max_length=5000)),
                ('contenido', models.TextField(default='DEFAULT_VALUE')),
                ('img_destacada', models.FileField(upload_to='')),
                ('slug', models.CharField(default='DEFAULT_VALUE', max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'entradas',
            },
        ),
    ]
