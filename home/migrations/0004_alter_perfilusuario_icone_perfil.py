# Generated by Django 4.2.5 on 2023-12-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='icone_perfil',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
