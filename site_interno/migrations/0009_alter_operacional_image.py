# Generated by Django 5.0.6 on 2024-06-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_interno', '0008_rename_descripiton_operacional_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacional',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imagens_operacionais/', verbose_name='Inserir Imagem'),
        ),
    ]