# Generated by Django 4.0 on 2021-12-16 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='DEFAULT_VALUE', max_length=1000)),
                ('img_perfil', models.FileField(upload_to='')),
                ('web', models.CharField(default='DEFAULT_VALUE', max_length=700)),
                ('descripcion', models.TextField()),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('updated_ad', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
    ]
